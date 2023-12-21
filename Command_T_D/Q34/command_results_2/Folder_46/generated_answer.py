import sys
from functools import reduce
def find_original_set(A):
    return reduce(lambda a,b:a|b,A)
