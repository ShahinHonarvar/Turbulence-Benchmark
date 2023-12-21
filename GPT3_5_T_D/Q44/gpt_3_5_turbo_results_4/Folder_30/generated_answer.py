
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_composite(n):
        return not is_prime(n)
    
    composite_set = set()
    for num in lst[19:93]:
        if is_composite(num):
            composite_set.add(num)
    
    return composite_set
