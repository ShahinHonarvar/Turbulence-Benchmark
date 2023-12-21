
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(74, min(96, len(numbers))):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])

    return composite_nums
