
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(56, 99):
        num = lst[i]
        if num < 2:
            continue
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                composites.add(num)
                break
    return composites
