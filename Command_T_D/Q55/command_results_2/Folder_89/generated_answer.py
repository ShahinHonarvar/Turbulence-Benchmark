import functools
@functools.lru_cache
def lists_with_product_equal_n(n):
    # Find all factors of n
    factors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            factors += [[i]]
            if i * i != n:
                factors += [[i, n // i]]
    # Filter out any that don't multiply to n
    filters = set()
    for f in factors:
        if f[0] * f[1] == n:
            filters.add(f)
    # Join any filters that have the same elements
    lists = []
    for f in filters:
        if len(f) > 1:
            lists += [[f[0], f[1]]
        else:
            lists += [[f]]
    # Add the single element lists
    lists += [f for f in filters if len(f) == 1]
    return lists
