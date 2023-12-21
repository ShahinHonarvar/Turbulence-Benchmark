
def composite_nums_between_indices(list_of_positive_integers):
    return {num for i, num in enumerate(list_of_positive_integers) if 37 <= i <= 76 and num > 1}
