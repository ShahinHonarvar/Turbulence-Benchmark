
def composite_nums_between_indices(my_list):
    composites = set()
    for i in range(75, 89):
        if my_list[i] > 1 and my_list[i] not in composites:
            composites.add(my_list[i])
    return composites
