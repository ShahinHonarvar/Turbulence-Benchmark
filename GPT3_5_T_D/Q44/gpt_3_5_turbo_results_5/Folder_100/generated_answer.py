
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_composite(n):
        return not is_prime(n)
    
    composites = set()
    for n in lst[12:93]:
        if is_composite(n):
            composites.add(n)
    
    return composites
