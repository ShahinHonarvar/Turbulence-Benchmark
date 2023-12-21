import re
def if_decimal_is_divisible(s):
    return int(s[::-1], 2) % 0x3C4B54B == 0
