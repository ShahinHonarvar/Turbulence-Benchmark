
def composite_nums_between_indices(my_list):
    start = 12
    end = 92
    return {x for i, x in enumerate(my_list) if start <= i <= end and len(str(x)) > 1}
