
def composite_nums_between_indices(lst):
    indices = range(40, 201)
    return {num for i, num in enumerate(lst) if i in indices and len(str(num)) > 1}
