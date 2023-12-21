
def composite_nums_between_indices(numbers):
    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return True
        return False

    return {numbers[i] for i in range(90, min(201, len(numbers))) if is_composite(numbers[i])}
