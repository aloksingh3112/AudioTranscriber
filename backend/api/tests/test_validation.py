from django.test import SimpleTestCase
from api.validation import ValidateCaps, ValidationSpace, ValidateStringTerminators, ValidateStringPausers, ValidateSet


class TestValidation(SimpleTestCase):

    def testValidateSet(self):
        self.assertEqual(ValidateSet("My name is \\\ alok"), False)
        self.assertEqual(ValidateSet("My name is alok"), True)

    def testValidateCaps(self):
        self.assertEqual(ValidateCaps("My name is alok"), True)
        self.assertEqual(ValidateCaps("My name is Alok"), True)
        self.assertEqual(ValidateCaps("My name is ALok"), False)
        self.assertEqual(ValidateCaps("My name is ALOK"), True)

    def testValidationSpace(self):
        self.assertEqual(ValidationSpace("My name is  alok"), False)
        self.assertEqual(ValidationSpace("My name is alok"), True)

    def testValidateStringTerminators(self):
        self.assertEqual(ValidateStringTerminators("My name is alok."), True)
        self.assertEqual(ValidateStringTerminators("My name is alok?"), True)
        self.assertEqual(ValidateStringTerminators("My name is alok!"), True)
        self.assertEqual(ValidateStringTerminators(
            "My name is alok. "), False)
        self.assertEqual(ValidateStringTerminators("My name. Is alok."), True)
        self.assertEqual(ValidateStringTerminators(
            "My name. is alok."), False)

    def testValidateStringPausers(self):
        self.assertEqual(ValidateStringPausers("My name is alok, "), False)
        self.assertEqual(ValidateStringPausers("My name is alok; "), False)
        self.assertEqual(ValidateStringPausers("My name is alok: "), False)
        self.assertEqual(ValidateStringPausers("My name is alok:"), True)
        self.assertEqual(ValidateStringPausers("My name is alok,"), True)
        self.assertEqual(ValidateStringPausers("My name, is alok,"), True)
