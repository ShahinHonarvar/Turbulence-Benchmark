
def composite_nums_between_indices(lst):
    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return True
        return False

    return set(filter(is_composite, lst[1:6]))
