
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 37 <= i <= 51 and x > 1}
