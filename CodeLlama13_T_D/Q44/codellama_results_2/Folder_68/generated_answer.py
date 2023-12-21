
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(9):
        if numbers[i] > 1 and numbers[i] % 2 != 0:
            composite_nums.add(numbers[i])
    return composite_nums
