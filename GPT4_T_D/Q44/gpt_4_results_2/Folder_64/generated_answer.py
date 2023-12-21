
def composite_nums_between_indices(lst):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return {n for i, n in enumerate(lst[:5]) if check_composite(n)}
