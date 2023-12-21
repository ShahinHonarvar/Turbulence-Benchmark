
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 6 <= i < 12 and x > 1}
