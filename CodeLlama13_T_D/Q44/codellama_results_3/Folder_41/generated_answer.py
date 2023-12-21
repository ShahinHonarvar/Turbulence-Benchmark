
def composite_nums_between_indices(list_of_ints):
    return {i for i in list_of_ints[0:3] if len(set(range(1, int(i**0.5) + 1))) > 2}
