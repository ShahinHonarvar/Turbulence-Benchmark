import functools
@functools.lru_cache(maxsize=40)
def find_original_set(X):
    return set(functools.chain.from_iterable(X))
