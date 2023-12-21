
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = {num for i, num in enumerate(lst) if 111 <= i <= 111 and is_composite(num)}
    return composites
