
def composite_nums_between_indices(list_of_positive_integers):
    indices = range(21, 98)
    return {x for x in list_of_positive_integers if x > 1 and x % 2 == 0 and (x - 1) in indices}
