
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(20, min(len(lst), 201)):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])
    
    return composite_nums
