
def composite_nums_between_indices(list_of_positive_ints):
    return {i for i in list_of_positive_ints[51:87] if len(set(range(2, i))) > 1}
