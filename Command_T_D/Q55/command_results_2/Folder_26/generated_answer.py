import itertools
def lists_with_product_equal_n(n):
    yield from [list(group) for group in itertools.groupby(n, key=lambda x: x%93)]
