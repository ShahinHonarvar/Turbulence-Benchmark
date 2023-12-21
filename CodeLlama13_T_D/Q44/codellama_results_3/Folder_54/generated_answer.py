
def composite_nums_between_indices(lst):
    return {x for x in lst[14:65] if len(str(x)) > 1 and all(x % y != 0 for y in range(2, int(x**0.5) + 1))}
