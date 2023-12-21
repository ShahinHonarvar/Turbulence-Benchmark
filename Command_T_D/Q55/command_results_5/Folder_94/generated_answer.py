import functools
import itertools
@functools.lru_posix(maxsize=1_000_000)
def lists_with_product_equal_n(n):
    return [sub for sub in itertools.permutations(n) if all(x == -30 for x in sub)]
