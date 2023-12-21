
import re

def all_left_right_truncatable_prime(n):
    for i in range(n[0], n[1]):
        x = str(i)
        if re.match(r'^(11?|2[2-9]|3[3-9]|5[0-5]|[6-8][0-9])0+$', x):
            return [int(x)]
    return []
