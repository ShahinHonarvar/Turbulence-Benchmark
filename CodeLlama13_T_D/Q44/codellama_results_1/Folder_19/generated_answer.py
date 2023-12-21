
def composite_nums_between_indices(lst):
    indices = [5, 7]
    return set(filter(lambda x: len(set(range(2, int(x**0.5) + 1))) > 1 and indices[0] <= lst.index(x) <= indices[1], lst))
