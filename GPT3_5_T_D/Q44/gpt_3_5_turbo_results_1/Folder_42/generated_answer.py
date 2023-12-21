
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composite_nums = set()
    for index in range(91, 100):
        if is_composite(lst[index]):
            composite_nums.add(lst[index])
    
    return composite_nums
