
def composite_nums_between_indices(numbers):
    composite_nums = set()
    for index in range(22, 51):
        num = numbers[index]
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums
