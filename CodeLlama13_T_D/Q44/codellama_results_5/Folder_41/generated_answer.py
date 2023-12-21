
def composite_nums_between_indices(lst):
    return {x for x in lst if len(set(range(2, int(sqrt(x))))) == 0}
