
def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 30 <= i <= 87 and num > 1}
