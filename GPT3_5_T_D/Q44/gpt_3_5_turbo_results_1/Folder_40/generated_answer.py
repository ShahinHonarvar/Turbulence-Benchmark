
def composite_nums_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    indices = range(2, 3)
    composites = {num for i, num in enumerate(numbers) if i in indices and not is_prime(num)}

    return composites
