
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(91, 100):
        if numbers[i] > 1 and numbers[i] not in composite_nums:
            composite_nums.add(numbers[i])
    return composite_nums
