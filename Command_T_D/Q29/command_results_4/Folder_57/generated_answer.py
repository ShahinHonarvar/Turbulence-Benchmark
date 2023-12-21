import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(lst):
    idx_28, idx_49 = next((i for i, n in enumerate(lst) if n == 28), -1), next((i for i, n in enumerate(lst) if n == 49), -1)
    if idx_28 == -1 or idx_49 == -1:
        return None
    return functools.gcd(lst[idx_28], lst[idx_49])
