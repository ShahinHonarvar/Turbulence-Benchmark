
import re

def all_left_right_truncatable_prime(x):
    # y = x - 1
    # while y >= 2:
    #     if all(str(x).count(str(n)) == 1 for n in range(2, y)):
    #         return [x - n for n in range(2, y)]
    #     y -= 1
    # return []
    strx = str(x)
    return sorted([x for x in range(2, x) if re.match(r'[13579][01][23456789]0', str(x))])
