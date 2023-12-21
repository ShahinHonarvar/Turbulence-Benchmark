
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    return set([i for i in lst[91:100] if is_composite(i)])
