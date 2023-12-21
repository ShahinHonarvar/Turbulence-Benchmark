from functools import reduce
from operator import and_
from functools import reduce
def find_original_set(x):
    return reduce(and_, (x for x in range(1, 100)))
