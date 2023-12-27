'''import unittest

from django.contrib import messages
from django.contrib.messages import constants

from .utils import password_is_valid


class PasswordIsValidTests(unittest.TestCase):

    def test_password_is_valid_with_empty_password(self):
        password = ''
        confirm_password = ''
        request = None

        result = password_is_valid(password, confirm_password, request)

        self.assertEqual(result, False)
        self.assertEqual(messages.get_messages(request)[0].level, constants.ERROR)

    def test_password_is_valid_with_short_password(self):
        password = '12345'
        confirm_password = '12345'
        request = None

        result = password_is_valid(password, confirm_password, request)

        self.assertEqual(result, False)
        self.assertEqual(messages.get_messages(request)[0].level, constants.ERROR)

    def test_password_is_valid_with_mismatched_passwords(self):
        password = '123456'
        confirm_password = '789012'
        request = None

        result = password_is_valid(password, confirm_password, request)

        self.assertEqual(result, False)
        self.assertEqual(messages.get_messages(request)[0].level, constants.ERROR)

    def test_password_is_valid_with_valid_password(self):
        password = '123456@#$'
        confirm_password = '123456@#$'
        request = None

        result = password_is_valid(password, confirm_password, request)

        self.assertEqual(result, True)


i
'''