
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(17, 79):
        if numbers[i] > 1 and numbers[i] not in composites:
            composites.add(numbers[i])
    return composites
