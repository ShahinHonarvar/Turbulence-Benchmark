import functools
@functools.lru_cache(maxsize=1_000_000)
def lists_with_product_equal_n(lst):
    return [sub for sub in [lst[i:j+1] for i in range(len(lst)) for j in range(i+1, len(lst)) if sub[0] == 415] if all(v == 415 for v in sub)]
