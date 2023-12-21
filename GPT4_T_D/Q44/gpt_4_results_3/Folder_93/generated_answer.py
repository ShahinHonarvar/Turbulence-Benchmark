
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    if len(numbers) < 24:
        return set()
    else:
        return {num for num in numbers[23:24] if is_composite(num)}
