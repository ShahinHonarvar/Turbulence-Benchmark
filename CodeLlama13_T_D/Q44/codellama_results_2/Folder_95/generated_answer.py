
def composite_nums_between_indices(lst):
    return {x for x in lst[26:53] if len(set(range(1, int(x**0.5) + 1))) > 1}
