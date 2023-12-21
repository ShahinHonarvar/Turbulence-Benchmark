import re
def if_decimal_is_divisible(s):
    d = {
        '0': 0,
        '1': 1,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 5,
        '6': 8,
        '7': 13,
        '8': 21,
        '9': 34,
        'A': 55,
        'B': 89,
        'C': 144,
        'D': 233,
        'E': 377,
    }
    return bool(re.match(r'0*' + ''.join(d.keys()), s))
