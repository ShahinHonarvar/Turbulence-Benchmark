
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(50, 201):
        num = lst[i]
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composites.add(num)
    return composites
