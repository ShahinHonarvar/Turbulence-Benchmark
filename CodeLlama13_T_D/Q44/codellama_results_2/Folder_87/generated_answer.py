
def composite_nums_between_indices(list_of_positive_ints):
    composites = set()
    for i in range(43, 52):
        if list_of_positive_ints[i] > 1:
            composites.add(list_of_positive_ints[i])
    return composites
