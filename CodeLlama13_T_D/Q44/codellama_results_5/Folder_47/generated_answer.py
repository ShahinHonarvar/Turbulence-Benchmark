
def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 75 <= i <= 88 and num > 1}
