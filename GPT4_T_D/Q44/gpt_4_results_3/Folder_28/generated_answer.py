
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = [i for i in lst[22:89] if is_composite(i)]
    
    return set(composite_nums)
