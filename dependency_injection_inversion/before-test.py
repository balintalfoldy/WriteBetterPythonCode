import unittest
from io import StringIO
from unittest.mock import patch
from before import *


class Authorizer_SMS_TestCase(unittest.TestCase):

    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())

    def test_code_decimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())

    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized())

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()
        self.assertFalse(auth.is_authorized())


#! really hard to test for success or failure cases because there is no way to directly set the code for testing
#! The problem is that the pay() method is responsible for creating the authorizer object, which means we can't
#! create the object in testcase and set some test value and then pass it to the pay method
#! unittest has a mock part in there libary, which allows you to create mock objects and replace object that are used
#! in functions with other obejct but is very complicated and will not work many time.
#! that is where dependency injection pattern comes into play -> introduce the dependency injection to improve the testability of the code.
class PaymentProcessor_TestCase(unittest.TestCase):

    def test_payment_success(self):
        # ???
        self.assertTrue(True)

    def test_payment_fail(self):
        # ???
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
