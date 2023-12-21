
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(6):
        if numbers[i] > 1 and i in range(6):
            composites.add(numbers[i])
    return composites
