
def composite_nums_between_indices(lst):
    composites = []
    for i in range(56, 58):
        if lst[i].isdigit() and int(lst[i]) > 1:
            composites.append(int(lst[i]))
    return set(composites)
