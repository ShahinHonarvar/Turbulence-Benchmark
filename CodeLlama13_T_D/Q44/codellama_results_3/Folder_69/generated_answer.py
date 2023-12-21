
def composite_nums_between_indices(arr):
    return {x for i, x in enumerate(arr) if 29 <= i <= 79 and x > 1}
