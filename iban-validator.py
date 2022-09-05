"""
Iban for testing:
LI21088100002324013AA
"""

iban = input('Please enter your iban: ')
# Used to verify country of the iban
country = iban[0:2]
country_codes = ['LI']
# Standard length for iban's from Lichtenstein
iban_length = 19
# Removes AA from the end of the iban code
iban = iban[:-2]
# Account number part of the iban
account_number = iban[12:]
# Test number for Lichtenstein
test_number = "1209000"
# Bank identifier part of the iban code
bank_identifier = iban[4:9]
# List of bank identity numbers from Lichtenstein
bank_identifiers = ["08801", "08802", "08803", "08804", "08805", "08806",
                    "08807", "08808", "08809", "08810", "08811", "08812",
                    "08813"]

"""
The checksum_validation is used to validate the iban against the checksum.
I got the information on how to calculate this from here:

https://www.ibancalculator.com/calculation.html

I modified this to work with iban's from Lichtenstein
"""

checksum_validation = 98 - int(bank_identifier + account_number +
                               test_number) % 97
checksum = iban[2:4]


def validate_iban():
    # I don't print any errors because this involves bank information.
    if country not in country_codes:
        return False
    if not iban_length == len(iban):
        return False
    if bank_identifier not in bank_identifiers:
        return False
    if not checksum_validation == int(checksum):
        return False
    else:
        return True


print(validate_iban())
