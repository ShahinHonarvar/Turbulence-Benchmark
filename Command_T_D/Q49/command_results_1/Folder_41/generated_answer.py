import re
def if_decimal_is_divisible(s):
    if re.match(r'0b[01]+0010011000011000011100101101', s):
        return True
    else:
        return False
