
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(0, 6):
        if lst[i] > 1 and len(str(lst[i])) > 1:
            composites.add(lst[i])
    return composites
