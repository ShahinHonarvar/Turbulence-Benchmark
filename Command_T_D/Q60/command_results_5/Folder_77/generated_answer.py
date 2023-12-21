
import re

def all_left_right_truncatable_prime(tup):
    x = tup[767]
    str_x = str(x)
    m = re.match(r"^[13579]*[13579][13579]*$", str_x)
    if m:
        return [int(n) for n in str_x[1:-1]]
    else:
        return []
