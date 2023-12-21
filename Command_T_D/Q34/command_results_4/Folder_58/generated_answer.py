from functools import reduce
from operator import and_
def find_original_set(S):
    return reduce(and_, (set(s) for s in S))
