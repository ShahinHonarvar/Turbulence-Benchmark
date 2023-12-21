import re
def if_decimal_is_divisible(binary):
    return bool(re.fullmatch(r'0*1*(10+\d)', binary))
