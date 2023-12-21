
def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if i >= 0 and i <= 8 and len(str(num)) > 1}
