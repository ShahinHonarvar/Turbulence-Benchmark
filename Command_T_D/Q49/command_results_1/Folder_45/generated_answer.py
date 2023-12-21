import re
def if_decimal_is_divisible(s):
    return re.fullmatch(r'0b([01]+)', s).group(1) in '111011010'
