
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return set([x for i, x in enumerate(numbers[:5]) if is_composite(x)])
