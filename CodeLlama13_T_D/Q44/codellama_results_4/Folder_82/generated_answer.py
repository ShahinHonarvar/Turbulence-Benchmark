
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 30 <= i < 31 and x > 1}
