
def composite_nums_between_indices(my_list):
    composites = set()
    for i in range(75, 95):
        if my_list[i] > 1:
            composites.add(my_list[i])
    return composites
