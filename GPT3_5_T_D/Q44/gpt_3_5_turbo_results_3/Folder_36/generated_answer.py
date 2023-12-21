
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composite_set = set()
    for num in lst[686:988]:
        if is_composite(num):
            composite_set.add(num)
    
    return composite_set
