# -*- coding: utf-8 -*-

import requests


class PostmonAPI():

    def __init__(self):
        self.baseurl = "http://api.postmon.com.br/v1/cep/"

    def get_address_by_zipcode(self, zipcode):

        resp = requests.get(self.baseurl + zipcode)

        if resp.status_code != 200:
            return

        data = resp.json()
        ret = {}

        ret['zip_code'] = data['cep']
        ret['neighborhood'] = data['bairro']
        ret['address'] = data['logradouro']
        ret['state'] = data['estado']
        ret['city'] = data['cidade']

        return ret

postmon = PostmonAPI()
