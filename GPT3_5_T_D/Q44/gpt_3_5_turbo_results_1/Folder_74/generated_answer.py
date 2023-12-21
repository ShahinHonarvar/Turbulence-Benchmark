
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(42, 69):
        if is_composite(lst[i]):
            composites.add(lst[i])
    
    return composites
