
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if 639 <= i <= 975 and isinstance(x, int) and x > 1}
