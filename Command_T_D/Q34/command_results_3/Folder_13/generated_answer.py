from functools import reduce
from operator import and_
from functools import reduce
def find_original_set(s):
    return reduce(and_,s)
