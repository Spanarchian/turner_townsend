"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""
from translater.to_arabic import verify_number_roman as vnr
from translater.to_arabic import convert2arabic as c2a


testdata = [['I',True], ['X',True], ['S', False], ['D',True], ['W',False], ['M',True],
            ['IV', True], ['VIII', True], ['XXX', True], ['S', False], ['D', True], ['W', False], ['MXC', True]]


def test_verify_number_roman():
    targetlist = testdata
    for target in targetlist:
        expected = target[1]
        actual = vnr(target[0])
        assert actual["status"] == expected, "ERROR:  Numeric {} not a Roman Numerical but system thinks it is".format(target[0])


testdata1 = [['I', 1], ['V', 5], ['XI', 11], ['D', 500], ['M',1000], ['X', 10], ['D', 500], ['MDXV',1515]]


def test_change_from_roman():
    targetlist = testdata1
    for target in targetlist:
        expected = "{} in Arabic it is {}". format(target[0], target[1])
        actual = c2a(target[0])
        assert actual == expected, "ERROR:  Numeric not a Roman Numerical but system thinks it is"


def test_with_non_roman_chars():
    """

    :return:
    """
    testdata1 = [['VW', 1], ['F', 5], ['Z', 10], ['OX', 500]]
    targetlist = testdata1
    for target in targetlist:
        expected = "Value supplied is not a roman numeral".format(target[0])
        actual = c2a(target[0])
    assert actual == expected, "ERROR:  Numeric not a Roman Numerical but system thinks it is"
