from functools import reduce
from operator import and_
def find_original_set(s):
    return reduce(and_, (s for s in range(1, 10**5+1)), set())
