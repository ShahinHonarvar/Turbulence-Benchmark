
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 25 <= i <= 87 and x > 1}
