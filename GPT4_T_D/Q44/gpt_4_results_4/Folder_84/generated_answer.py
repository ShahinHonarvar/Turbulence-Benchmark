
def composite_nums_between_indices(lst):
    composites = set()
    for num in lst[30:49]:
        if num > 1 and not all(num % i for i in range(2, int(num**0.5) + 1)):
            composites.add(num)
    return composites
