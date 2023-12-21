
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(56, 58):
        if numbers[i].is_composite():
            composites.add(numbers[i])
    return composites
