
def composite_nums_between_indices(list_of_positive_integers):
    return {number for index, number in enumerate(list_of_positive_integers) if 34 <= index <= 55 and number > 1}
