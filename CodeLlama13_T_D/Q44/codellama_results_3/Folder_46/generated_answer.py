
def composite_nums_between_indices(my_list):
    indices = range(28, 39)
    return set(x for i, x in enumerate(my_list) if i in indices and x > 1)
