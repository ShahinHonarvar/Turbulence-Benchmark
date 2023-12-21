
def composite_nums_between_indices(my_list):
    return {x for x in my_list[1:8+1] if len({2, 3, 5, 7} & set(str(x))) > 0}
