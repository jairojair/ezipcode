# -*- coding: utf-8 -*-

from unittest import TestCase
from application.app import app, db
import json


class TestZipCodeResource(TestCase):

    def setUp(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.c = app.test_client()
        db.create_all(app=app)

    def tearDown(self):

        db.session.remove()
        db.drop_all(app=app)

    """
    Get lists
    """

    def test_list(self):

        r = self.c.get('/zipcode/')
        self.assertEqual(r.status_code, 200)

    def test_list_by_limit(self):
        self.create('14020260', 201)
        self.create('88104-710', 201)
        self.create('88080-300', 201)
        r = self.c.get('/zipcode/?limit=2')
        self.assertEqual(r.status_code, 200)

    def test_list_invalid_limit(self):
        r = self.c.get('/zipcode/?limit=-1')
        self.assertEqual(r.status_code, 400)

    """
    Get
    """

    def get(self, zipcode, status):
        r = self.c.get('/zipcode/%s/' % zipcode)
        self.assertEqual(r.status_code, status)

    def test_get_zipcode(self):
        self.test_create_zipcode()
        self.get('14020260', 200)

    def test_get_zipcode_not_found(self):
        self.get('14020260', 404)

    def test_get_invalid_zipcode_format(self):
        self.get('1402026y', 400)

    """
    Create
    """

    def create(self, zipcode, status):
        data = json.dumps(dict(zip_code=zipcode))
        r = self.c.post('/zipcode/', data=data)
        self.assertEqual(r.status_code, status)

    def test_create_zipcode(self):
        self.create('14020260', 201)

    def test_create_zipcode_with_dash(self):
        self.create('14020-260', 201)

    def test_create_invalid_zipcode_by_postmon(self):
        self.create('14020261', 404)

    def test_create_invalid_zipcode_format(self):
        self.create('1402026y', 400)

    def test_create_invalid_zipcode_num_digits_1(self):
        self.create('-1', 400)

    def test_create_invalid_zipcode_num_digits_2(self):
        self.create('123456789', 400)

    def test_create_zipcode_already_existing(self):
        self.test_create_zipcode()
        self.test_create_zipcode()

    """
    Delete
    """

    def delete(self, zipcode, status):
        r = self.c.delete('/zipcode/%s/' % zipcode)
        self.assertEqual(r.status_code, status)

    def test_delete_zipcode(self):
        self.test_create_zipcode()
        self.delete('14020260', 204)

    def test_delete_invalid_zipcode(self):
        self.delete('1402026x', 400)

    def test_delete_zipcode_not_found(self):
        self.delete('14020260', 404)

    """
    URLs
    """

    def test_url_not_found(self):
        r = self.c.get('/DonkeyKong')
        self.assertEqual(r.status_code, 404)
