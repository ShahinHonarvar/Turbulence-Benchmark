
def composite_nums_between_indices(my_list):
    return {x for x in my_list if 10 <= my_list.index(x) <= 66 and len({2,3,5,7}.intersection([x])) > 1}
