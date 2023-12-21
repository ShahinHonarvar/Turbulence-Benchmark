
def composite_nums_between_indices(numbers):
    composites = []
    for i in range(91, 100):
        if numbers[i] > 1 and numbers[i] % numbers[i-1] == 0:
            composites.append(numbers[i])
    return set(composites)
