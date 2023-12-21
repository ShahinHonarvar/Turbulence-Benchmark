
def composite_nums_between_indices(numbers):
    if len(numbers) == 0:
        return set()
    
    start, end = 314, 347
    composites = set()
    for i in range(start, end + 1):
        if numbers[i] > 1 and i not in composites:
            composites.add(numbers[i])
    
    return composites
