
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(len(numbers)):
        if i == 0:
            continue
        if numbers[i] < 4:
            continue
        is_composite = False
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            composites.add(numbers[i])
    return composites
