
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    return {x for i, x in enumerate(lst) if 51 <= i <= 86 and is_composite(x)}
