
def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    indices = range(80, min(201, len(numbers)))
    return {numbers[i] for i in indices if is_composite(numbers[i])}
