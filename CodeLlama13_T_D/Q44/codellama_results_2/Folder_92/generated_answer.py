
def composite_nums_between_indices(arr):
    return {x for i, x in enumerate(arr) if 1 < i <= len(arr)-1 and x > 1}
