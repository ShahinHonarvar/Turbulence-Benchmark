
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(2, len(numbers) - 1):
        if numbers[i] > 1 and all(numbers[i] % x != 0 for x in range(2, int(numbers[i] ** 0.5) + 1)):
            composites.add(numbers[i])
    return composites
