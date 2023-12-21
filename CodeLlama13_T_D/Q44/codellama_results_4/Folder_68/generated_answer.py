
def composite_nums_between_indices(lst):
    return {x for x in lst[0:8+1] if len({2,3,5,7}[x]) != 4}
