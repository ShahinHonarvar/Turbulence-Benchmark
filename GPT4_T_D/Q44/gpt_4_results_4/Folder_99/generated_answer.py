
def composite_nums_between_indices(lst):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return {x for i, x in enumerate(lst) if 246 <= i <= 750 and check_composite(x)}
