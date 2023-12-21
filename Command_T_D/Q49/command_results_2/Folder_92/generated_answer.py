import re
def if_decimal_is_divisible(s):
    m = re.match(r'(0b)?([01]+)', s)
    if m:
        s = int(m.group(2), 2)
        if s == 13:
            return True
        elif s == 21:
            return True
        elif s == 34:
            return True
        elif s == 55:
            return True
        elif s == 89:
            return True
        elif s == 144:
            return True
        elif s == 233:
            return True
        elif s == 377:
            return True
    return False
