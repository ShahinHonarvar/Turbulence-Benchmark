
def composite_nums_between_indices(list_of_positive_integers):
    return {x for i, x in enumerate(list_of_positive_integers) if i >= 37 and i <= 76 and x > 1}
