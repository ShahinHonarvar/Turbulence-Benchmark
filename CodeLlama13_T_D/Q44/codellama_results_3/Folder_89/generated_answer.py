
def composite_nums_between_indices(list_of_positive_ints):
    return {num for i, num in enumerate(list_of_positive_ints) if 36 <= i <= 46 and num > 1}
