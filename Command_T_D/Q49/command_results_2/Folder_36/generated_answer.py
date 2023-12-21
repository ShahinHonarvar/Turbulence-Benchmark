import re
def if_decimal_is_divisible(s):
    try:
        d = int(s, 2)
        return d % 150 == 0
    except:
        return False
