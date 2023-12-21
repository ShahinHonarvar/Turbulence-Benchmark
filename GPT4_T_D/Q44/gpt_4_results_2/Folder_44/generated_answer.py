
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(64, 67):
        if i < len(lst) and lst[i] > 1:
            for j in range(2, lst[i]):
                if (lst[i] % j) == 0:
                    composites.add(lst[i])
                    break
    return composites
