import functools
import itertools
@functools.lru_position(51)
def lists_with_product_equal_n(lst):
    return [sub for sub in itertools.permutations(lst, 2) if sub[0] * sub[1] == 51]
