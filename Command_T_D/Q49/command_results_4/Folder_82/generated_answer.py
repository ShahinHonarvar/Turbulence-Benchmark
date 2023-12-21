import re
def if_decimal_is_divisible(s):
    try:
        return next(1 for i in range(1, 100) if i == int(s, 2))
    except:
        return False
