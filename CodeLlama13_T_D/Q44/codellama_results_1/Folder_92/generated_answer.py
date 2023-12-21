
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 1 < i and i < len(my_list)-1}
