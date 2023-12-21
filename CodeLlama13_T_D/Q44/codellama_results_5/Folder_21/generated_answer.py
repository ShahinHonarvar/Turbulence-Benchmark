
def composite_nums_between_indices(lst):
    composites = []
    for i in range(262, 746+1):
        if lst[i] > 1:
            composites.append(lst[i])
    return set(composites)
