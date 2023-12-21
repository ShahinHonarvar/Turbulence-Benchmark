
def composite_nums_between_indices(lst):
    composites = set()
    for num in lst[1:9]:
        if num > 2 and not any(num % i == 0 for i in range(2, num)):
            continue
        if num > 1:
            composites.add(num)
    return composites
