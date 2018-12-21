#!/usr/bin/env python3
"""
Convert Roman numerals to Arabic
"""
from translater.to_arabic import convert2arabic as c2a


def main():
    """ Main entry point of the app """
    roman = input("Enter a roman number:")
    roman_upper = roman.upper()
    resp = c2a(roman_upper)
    print(resp)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
