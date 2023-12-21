import sys
from functools import reduce
def find_original_set(s):
    # print(s)
    return reduce(lambda x, y: x|y, s)
