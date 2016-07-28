# -*- coding: utf-8 -*-

from unittest import TestCase
from application.app import app


class TestZipCodeResource(TestCase):

    def setUp(self):
        self.c = app.test_client()

    def test_index(self):
        r = self.c.get('/')
        self.assertEqual(r.status_code, 200)

    def test_not_found(self):
        r = self.c.get('/DonkeyKong')
        self.assertEqual(r.status_code, 404)
