import re
def if_decimal_is_divisible(s):
    try:
        return 1 / int(s, 2) == 0.5
    except ZeroDivisionError:
        return False
