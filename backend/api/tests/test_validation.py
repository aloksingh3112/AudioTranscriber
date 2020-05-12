from django.test import SimpleTestCase
from api.validation import ValidateCaps, ValidationSpace, ValidateStringTerminators, ValidateStringPausers, ValidateSet


class TestValidation(SimpleTestCase):

    def testValidateSet(self):
        print(self)
        self.assertEquals(ValidateSet("My name is \\\ alok"), True)

    def testValidateCaps(self):
        print(self)
        self.assertEquals(ValidateCaps("My name is alok"), True)

    def testValidationSpace(self):
        self.assertEquals(ValidationSpace("My name is  alok"), False)

    def testValidateStringTerminators(self):
        self.assertEquals(ValidateStringTerminators("My name is alok."), True)

    def testValidateStringPausers(self):
        self.assertEquals(ValidateStringPausers("My name is alok,"), False)
