
def composite_nums_between_indices(lst):
    composites = []
    for i in range(40, 81):
        if len(str(lst[i])) > 1:
            composites.append(lst[i])
    return set(composites)
