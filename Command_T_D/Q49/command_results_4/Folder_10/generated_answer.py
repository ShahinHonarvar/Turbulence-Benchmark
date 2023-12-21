import re
def if_decimal_is_divisible(s):
    try:
        v = int(s, 2)
        if v < 0:
            return False
        if v == 0:
            return True
        return v % 2 == 0
    except:
        return False
    return v % 2 == 0
