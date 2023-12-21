
def composite_nums_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_composite(num):
        return not is_prime(num)

    composite_numbers = set()
    for i, num in enumerate(numbers):
        if 69 <= i <= 83 and is_composite(num):
            composite_numbers.add(num)

    return composite_numbers
