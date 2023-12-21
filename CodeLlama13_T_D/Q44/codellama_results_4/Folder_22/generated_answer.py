
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(50, 201):
        if len(set(str(i))) > 1:
            composites.add(i)
    return composites
