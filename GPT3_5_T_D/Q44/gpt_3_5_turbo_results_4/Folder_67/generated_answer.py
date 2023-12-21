
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for index, num in enumerate(numbers[56:83], 56):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    composite_nums.add(index)
                    break
    return composite_nums
