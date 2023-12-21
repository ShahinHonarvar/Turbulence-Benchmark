from functools import reduce
from operator import and_
def find_original_set(s):
    return reduce(and_, s)
