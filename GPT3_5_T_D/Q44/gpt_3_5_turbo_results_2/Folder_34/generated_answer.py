
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(70, 201):
        if all(i % n != 0 for n in range(2, int(i ** 0.5) + 1)):
            continue
        composites.add(numbers[i])
    return composites
