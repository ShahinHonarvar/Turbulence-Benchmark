
def composite_nums_between_indices(numbers):
    composites = []
    for i in range(80, 201):
        if numbers[i] > 1 and numbers[i] not in composites:
            composites.append(numbers[i])
    return set(composites)
