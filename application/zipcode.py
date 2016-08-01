# -*- coding: utf-8 -*-

import logging
import re

from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer
from restless.exceptions import NotFound, BadRequest

from application.models import ZipCodeModel
from application.integrations import postmon


logger = logging.getLogger(__name__)
handler = logging.FileHandler('ezipcode.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ZipCodeResource(FlaskResource):

    preparer = FieldsPreparer(fields={
        'zip_code': 'zip_code',
        'address': 'address',
        'neighborhood': 'neighborhood',
        'state': 'state',
        'city': 'city'
    })

    def is_authenticated(self):
        return True

    def __get_zipcode(self, zipcode):
        return ZipCodeModel.query.filter_by(zip_code=zipcode).first()

    def list(self):
        """ list all """

        logger.info('Listing zipcodes')

        limit = self.request.args.get('limit')
        self.check_is_valid_limit(limit)

        zipcodes = ZipCodeModel.query.limit(limit).all()

        ret = []

        for zipcode in zipcodes:
            ret.append(zipcode)

        return ret

    def create(self):
        """ create zipcode """

        code = self.data['zip_code']
        self.check_is_valid(code)

        zipcode = self.__get_zipcode(code)

        if zipcode is None:

            logger.info('Zipcode %s not found in database' % code)
            logger.info('Searching zipcode %s in postmon' % code)

            resp = postmon.get_address_by_zipcode(code)

            if resp is None:
                logger.info('Zipcode %s not found in postmon' % code)
                raise NotFound(msg="Zipcode %s not found." % code)

            zipcode = ZipCodeModel(**resp)
            zipcode.save()
            logger.info("Zipcode %s saved" % zipcode.zip_code)
            return

        logger.info('Zipcode %s already exists in database' % zipcode.zip_code)

    def detail(self, pk):
        """ return zipcode """

        self.check_is_valid(pk)
        zipcode = self.__get_zipcode(pk)

        if zipcode is None:
            logger.info('Zipcode %s not found in database' % pk)
            raise NotFound(msg="Zipcode %s not found in database" % pk)

        return zipcode

    def delete(self, pk):
        """ delete zipcode """

        self.check_is_valid(pk)
        zipcode = self.detail(pk)
        zipcode.delete()
        logger.info('Zipcode %s deleted' % zipcode.zip_code)

    def check_is_valid(self, zipcode):
        """ check is valid zipcode """

        if zipcode is None:

            logger.info('zip_code field it was not filled.')
            raise BadRequest(msg="Field zip_code is required.")

        # remove - of string
        zipcode = re.sub('-', '', zipcode)

        if re.match(r'^[0-9]{8}$', zipcode) is None:

            logger.info('Zipcode %s is invalid' % zipcode)
            raise BadRequest(msg="Invalid zipcode")

    def check_is_valid_limit(self, limit):
        """ check is valid limit """

        if limit is None:
            return

        if re.match(r'^[0-9]+$', limit) is None:
            logger.info('Limit %s is invalid' % limit)
            raise BadRequest(msg="Invalid limit value")
