
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(533, 606):
        num = lst[i]
        if num > 1 and any(num % j == 0 for j in range(2, int(num ** 0.5) + 1)):
            composites.add(num)
    return composites
