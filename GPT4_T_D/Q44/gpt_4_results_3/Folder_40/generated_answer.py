
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(2, 3):
        num = lst[i]
        if num > 1:
            for j in range(2,num):
                if (num % j) == 0:
                    composites.add(num)
                    break
    return composites
