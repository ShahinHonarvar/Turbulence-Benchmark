
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(50, 55):
        num = lst[i]
        if num > 1:
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    composites.add(num)
                    break
    return composites
