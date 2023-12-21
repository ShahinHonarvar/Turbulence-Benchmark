
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    return set(n for n in lst[4:5] if is_composite(n))
