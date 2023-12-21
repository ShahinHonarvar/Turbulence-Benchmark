
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return set([n for n in numbers[4:5] if is_composite(n)])
