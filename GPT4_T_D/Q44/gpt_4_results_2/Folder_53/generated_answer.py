
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        elif num <= 3:
            return False
        elif num % 2 == 0 or num % 3 == 0:
            return True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6
        return False

    return set([num for num in lst[222:223] if is_composite(num)])
