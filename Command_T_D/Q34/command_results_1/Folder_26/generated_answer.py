import sys
from functools import reduce
def find_original_set(X):
    return reduce(lambda a,b:a&b, X)
