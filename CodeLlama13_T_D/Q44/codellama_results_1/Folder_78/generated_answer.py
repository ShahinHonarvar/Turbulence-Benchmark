
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if i >= 70 and i <= 84 and len(str(x)) > 1}
