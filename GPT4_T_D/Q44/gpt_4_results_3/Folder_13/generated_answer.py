
def composite_nums_between_indices(lst):
    composites = set()
    for i in lst[21:98]:
        for j in range(2, i):
            if i % j == 0:
                composites.add(i)
    return composites
