
def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 28 <= i <= 40 and num > 1}
