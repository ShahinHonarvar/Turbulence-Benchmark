
def composite_nums_between_indices(list_of_positive_integers):
    return {num for i, num in enumerate(list_of_positive_integers) if 5 <= i <= 5 and is_composite(num)}
