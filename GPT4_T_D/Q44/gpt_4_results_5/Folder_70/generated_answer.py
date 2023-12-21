
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    if len(lst) < 36:
        return set()
    else:
        return set(el for el in lst[32:36] if is_composite(el))
