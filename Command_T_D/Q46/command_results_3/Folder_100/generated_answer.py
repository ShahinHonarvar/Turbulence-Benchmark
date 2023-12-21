
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return functools.reduce(gcf, lst[:3])

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
