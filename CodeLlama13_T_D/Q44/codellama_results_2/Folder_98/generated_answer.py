
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if i >= 0 and i <= 6 and x > 1}
