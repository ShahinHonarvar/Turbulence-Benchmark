import functools
@functools.lru_cache(maxsize=478)
def find_original_set(s):
    return set(s)
