import re

def checkPostValidation(postcode):
    res = re.match(r"\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b", postcode)
    if res:
        return "Correct"
    return "Wrong"

def checkCodeValidation(code):
    reg = "^(?=.*\d)[A-Za-z\d]{8,20}$"
    pattern = re.compile(reg)
    mat = re.search(pattern, code)

    if mat:
        return "Correct"
    return "Wrong"

if __name__ == "__main__":
    postcode = "1781943333"
    print (checkPostValidation(postcode))

    code = "baekhyun"
    print(checkCodeValidation(code))
