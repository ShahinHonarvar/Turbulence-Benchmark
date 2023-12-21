import functools
@functools.lru_cache(maxsize=1)
def find_subset_of_length_n(s):
    if not s:
        return 1
    return find_subset_of_length_n(s[:-1]) + find_subset_of_length_n(s[1:])
