
def composite_nums_between_indices(list_of_positive_ints):
    return set(filter(lambda x: 70 <= list_of_positive_ints.index(x) <= 84 and len(str(x)) > 1, list_of_positive_ints))
