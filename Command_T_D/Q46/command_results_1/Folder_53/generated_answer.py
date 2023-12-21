
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(lst):
    return max(gcf(a, b, c) for a, b, c in zip(lst, lst[1:], lst[2:]))

def gcf(a, b, c):
    if b == 0:
        return a
    elif c == 0:
        return b
    else:
        return gcf(b, c, a % b == 0 and a / b)
