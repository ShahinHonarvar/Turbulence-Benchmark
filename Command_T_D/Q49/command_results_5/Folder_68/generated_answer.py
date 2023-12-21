import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0b)?' + s[::-1] + r'\b', '0b' + ''.join(str(x) for x in range(1, int(1e9) + 1)) + '\b'))
