
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
        return False
    return set([num for num in lst[82:87] if is_composite(num)])
