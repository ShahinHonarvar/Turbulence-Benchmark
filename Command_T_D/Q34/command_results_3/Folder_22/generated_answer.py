import functools
@functools.lru_cache(maxsize=1)
def find_original_set(x):
    if x in set(range(1,26)):
        return {x}
    elif len(x) == 1:
        return {x}
    else:
        return {x, find_original_set(list(range(x[0],x[1])))}
