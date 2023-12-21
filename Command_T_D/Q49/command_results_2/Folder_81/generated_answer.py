import re
def if_decimal_is_divisible(s):
    return s.count('1') == 1 and int(s, 2) % 548 == 0
