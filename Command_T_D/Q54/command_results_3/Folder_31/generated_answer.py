import re
import sys
def all_right_truncatable_prime(x):
    x = str(x)
    x = re.sub("0*$", "", x)
    x = re.sub("0*$", "", x)
    x = re.sub("0*$", "", x)
    if x in range(2, int(x) + 1):
        return [int(x)]
    else:
        return []
