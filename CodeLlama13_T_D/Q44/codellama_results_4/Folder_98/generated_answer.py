
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(0, 7):
        if numbers[i] > 1:
            composites.add(numbers[i])
    return composites
