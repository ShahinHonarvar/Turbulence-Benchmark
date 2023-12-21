
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(5, 6):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])
    return composite_nums
