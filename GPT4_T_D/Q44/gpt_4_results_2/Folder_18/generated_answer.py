
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(25, 88):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if (lst[i] % j) == 0:
                    composites.add(lst[i])
                    break
    return composites
