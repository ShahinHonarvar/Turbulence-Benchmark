
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(1, len(numbers)):
        if numbers[i] > 1 and isinstance(numbers[i], int):
            composite_nums.add(numbers[i])
    return composite_nums
