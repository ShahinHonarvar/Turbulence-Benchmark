import set
def composite_nums_between_indices(lst):
    return set(filter(lambda x: is_composite(x), lst[37:76]))
def is_composite(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 5:
        return False
    if n == 4 or n == 6:
        return True
    return any(n % d == 0 for d in range(2, int(n ** .5) + 1))
