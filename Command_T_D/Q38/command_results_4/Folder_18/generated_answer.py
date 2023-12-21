import functools
@functools.lru_cache(maxsize=1)
def find_subset_of_length_n(s):
    return functools.reduce(lambda x, y: x + y, (1 for i in range(630) if i < len(s)), 1)
