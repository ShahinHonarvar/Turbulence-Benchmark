
def composite_nums_between_indices(lst):
    return {i for i in lst[2:3] if len(set(range(2, i))) > 1}
