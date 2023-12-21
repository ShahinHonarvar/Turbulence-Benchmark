
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 91 <= i <= 99 and x > 1}
