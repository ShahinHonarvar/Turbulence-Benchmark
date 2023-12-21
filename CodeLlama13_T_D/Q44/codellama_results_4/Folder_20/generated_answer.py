
def composite_nums_between_indices(numbers):
    indices = range(74, 96)
    composites = set()
    for i in indices:
        if numbers[i] > 1:
            composites.add(numbers[i])
    return composites
