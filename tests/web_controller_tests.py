#!/usr/bin/env python3
import unittest
from webtest import TestApp
from controllers import server


class WebControllerTests(unittest.TestCase):

    def test_home(self):
        app = TestApp(server)

        assert app.get('/').status == '200 OK'

    def test_select_image(self):
        app = TestApp(server)

        assert app.get('/select_image').status == '200 OK'


