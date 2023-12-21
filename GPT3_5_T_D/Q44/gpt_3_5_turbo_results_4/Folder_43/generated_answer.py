
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(31, 73):
        if any(i % j == 0 for j in range(2, int(i**0.5) + 1)):
            composites.add(lst[i])
    return composites
