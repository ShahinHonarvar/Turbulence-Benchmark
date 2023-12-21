
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    return {lst[i] for i in range(1, 2) if is_composite(lst[i])}
