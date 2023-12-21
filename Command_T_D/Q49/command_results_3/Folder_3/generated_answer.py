import re
def if_decimal_is_divisible(s):
    try:
        return 1 == int(s, 2) and (10**31 - 1) % 35 == int(s, 2)
    except:
        return False
