
def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst) if 51 <= i <= 86 and num > 1}
