
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    start = 36
    end = 46
    composite_nums = set()
    for i in range(start, end + 1):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])

    return composite_nums
