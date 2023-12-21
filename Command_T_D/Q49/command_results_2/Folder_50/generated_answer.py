import re
def if_decimal_is_divisible(s):
    if re.fullmatch(r'0*1*0*', s):
        return True
    return False
