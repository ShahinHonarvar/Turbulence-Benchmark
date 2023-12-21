
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    return set([num for num in lst[6:7] if is_composite(num)])
