
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(37, 77):
        if numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    composite_nums.add(numbers[i])
                    break
    return composite_nums
