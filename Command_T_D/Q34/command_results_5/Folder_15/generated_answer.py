import sys
from functools import reduce
from operator import and_, or_
def find_original_set(s1, s2):
    return reduce(or_, (s1, s2))
