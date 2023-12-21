import functools
@functools.lru_cache(maxsize=1_000_000)
def find_subset_of_length_n(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 1_000_000 * find_subset_of_length_n(n - 1) + find_subset_of_length_n(n - 2)
