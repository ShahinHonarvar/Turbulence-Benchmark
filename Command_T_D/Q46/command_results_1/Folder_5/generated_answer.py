
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(lambda x, y: (x, y) if x % y == 0 else x, lst[:3])
