
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(1, 6):
        num = numbers[i]
        if num > 1:
            composite_nums.add(num)
    return composite_nums
