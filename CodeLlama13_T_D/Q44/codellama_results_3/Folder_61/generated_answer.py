
def composite_nums_between_indices(numbers):
    composite_nums = []
    for i in range(8):
        if numbers[i] > 1 and numbers[i] <= len(numbers):
            composite_nums.append(numbers[i])
    return set(composite_nums)
