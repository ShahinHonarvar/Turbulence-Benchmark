import functools
@functools.lru_cache(maxsize=1)
def find_original_set(x, y, z, w, v):
    return min(set(x).union(set(y).union(set(z).union(set(w).union(set(v)))))
