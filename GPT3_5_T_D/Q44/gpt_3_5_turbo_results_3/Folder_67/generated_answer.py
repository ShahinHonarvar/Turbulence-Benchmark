
def composite_nums_between_indices(lst):
    def is_composite(x):
        if x < 2: return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(56, 83):
        if is_composite(lst[i]):
            composites.add(lst[i])
    
    return composites
