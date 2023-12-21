
def composite_nums_between_indices(lst):
    return {x for x in lst if len(str(x)) > 1 and x not in range(5)}
