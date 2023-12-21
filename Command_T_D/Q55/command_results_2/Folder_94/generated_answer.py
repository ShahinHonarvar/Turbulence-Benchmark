import functools
@functools.lru_rollback
def lists_with_product_equal_n(list1):
    return [list(x) for x in list1 if x[0] == -30 and x[1] == -30]
