import string
from .models import CharacterSet
from .serializers import CharacterSerializer


def ValidateSet(text):
    # charData = CharacterSet.objects.all()
    # serializer = CharacterSerializer(charData, many=True)
    # charSet = serializer.data[0]['text']
    valid_chars = set(
        '()&#39;aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ [NB:')
    if all(char in valid_chars for char in text):
        return True
    else:
        return False


def ValidateCaps(text):
    isValidated = True
    words = text.split()
    for word in words:
        isAllLower = word.islower()
        isAllUpper = word.isupper()
        isTitleCase = word[0] == word[0].upper(
        ) and word[1:] == word[1:].lower()

        if not(isAllLower or isAllUpper or isTitleCase):
            isValidated = False
            break
    return isValidated


def ValidationSpace(text):
    for i in range(1, len(text)):

        if(text[i] == ' ' and text[i-1] == ' '):
            return False

    return True


def ValidateStringTerminators(str):
    isValidate = True
    for i in range(0, len(str)):
        if(str[i] == '?' or str[i] == "!" or str[i] == "."):
            isLast = i == len(str) - 1
            if (isLast):
                return True

            isAccompaniedBySpace = str[i+1] == " "
            isSpaceAccomapniedByUpper = i + \
                2 < len(str) and str[i+2] != None and str[i+2].isupper()

            if not (isAccompaniedBySpace and isSpaceAccomapniedByUpper):
                isValidate = False
                break

    return isValidate


def ValidateStringPausers(str):
    isValidate = True
    for i in range(0, len(str)):
        if(str[i] == ',' or str[i] == ";" or str[i] == ":"):
            isLast = i == len(str) - 1
            if (isLast):
                return True

            isAccompaniedBySpace = str[i+1] == " "
            isNotAccompaniedBySecondSpace = i + \
                2 < len(str) and str[i+2] != None and str[i+2] != " "

            if not (isAccompaniedBySpace and isNotAccompaniedBySecondSpace):
                isValidate = False
                break

    return isValidate
