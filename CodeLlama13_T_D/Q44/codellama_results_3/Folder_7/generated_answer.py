
def composite_nums_between_indices(my_list):
    return {x for i, x in enumerate(my_list) if i >= 527 and i <= 538 and len(str(x)) > 1}
