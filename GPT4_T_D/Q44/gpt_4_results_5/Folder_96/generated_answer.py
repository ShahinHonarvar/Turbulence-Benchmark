
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(60, min(201, len(numbers))):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])
    return composite_nums
