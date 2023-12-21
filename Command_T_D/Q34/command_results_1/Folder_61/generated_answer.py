import functools
@functools.lru_cache(maxsize=1)
def find_original_set(X,Y,Z,W):
    return set(min(set(X).union(set(Y)).union(set(Z)).union(set(W)), key=len)
