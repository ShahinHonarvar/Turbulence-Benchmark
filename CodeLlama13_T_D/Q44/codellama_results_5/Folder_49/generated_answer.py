
def composite_nums_between_indices(list):
    return {x for x in list if 90 <= list.index(x) <= 200 and len({2, 3, 5, 7}.intersection(set(str(x)))) > 1}
