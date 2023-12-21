
def composite_nums_between_indices(my_list):
    indices = range(686, 987)
    composites = set()
    for i in indices:
        if my_list[i] > 1 and my_list[i] not in composites:
            composites.add(my_list[i])
    return composites
