import re
def if_decimal_is_divisible(s):
    return (int(s, 2) % 100000000000000) in range(1, 1000 + 1)
