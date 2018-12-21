roman_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def verify_number_roman(num):
    """To verify only Roman numerals are submitted"""
    valid = True
    resp = {"status": valid, "msg": "Value supplied is roman"}
    # Validate Value supplied
    if num == "":
        valid = False
        resp = {"status": valid, "msg": "No value supplied"}
    else:
        # Validate all chars are roman numerals
        for x in num:
            if x not in roman_nums:
                valid = False
                resp = {"status": valid, "msg": "Value supplied is not a roman numeral"}
    return resp


def convert2arabic(roman):
    verified = verify_number_roman(roman)

    if verified["status"] is not True:
        resp = verified["msg"]
        return resp

    # Perform calculation/transformation
    numb = 0
    for l in roman:
        numb = numb + roman_nums[l]
    resp = "{} in Arabic it is {}".format(roman, numb)
    return resp
