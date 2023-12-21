
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(52, 72):
        num = numbers[i]
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    composite_nums.add(num)
                    break
    return composite_nums
