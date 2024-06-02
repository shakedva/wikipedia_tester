import re


def validate_input(input):
    return re.match("^[A-Za-z ]+$", input)
