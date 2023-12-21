
def composite_nums_between_indices(mylist):
    composites = set()
    for i in range(5, 8):
        if mylist[i] > 1:
            composites.add(mylist[i])
    return composites
