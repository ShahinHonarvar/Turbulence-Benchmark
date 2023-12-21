
def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(43, 87):
        if numbers[i] > 1:
            composite_set.add(numbers[i])
    return composite_set
