
def composite_nums_between_indices(my_list):
    composites = []
    for i in range(70, 201):
        if my_list[i] > 1:
            composites.append(my_list[i])
    return set(composites)
