
def composite_nums_between_indices(list_of_positive_ints):
    return set(filter(lambda x: x > 40 and x < 81 and not isinstance(x, int), list_of_positive_ints))
