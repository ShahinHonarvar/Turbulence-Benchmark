
def composite_nums_between_indices(lst):
    def composite(n):
        if n <= 1:
            return False
        elif n == 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return True
            return False
            
    return set(x for x in lst[51:87] if composite(x))
