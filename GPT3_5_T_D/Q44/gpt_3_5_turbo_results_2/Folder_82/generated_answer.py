
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(30, 31):
        if numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    composites.add(numbers[i])
                    break
    return composites
