import set
def composite_nums_between_indices(lst):
    return set.set(''.join(str(n) for n in lst))
