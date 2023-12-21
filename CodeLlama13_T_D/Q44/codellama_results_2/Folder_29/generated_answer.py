
def composite_nums_between_indices(lst):
    indices = range(52, 71+1)
    return {x for x in lst if all(x % i != 0 for i in indices)}
