
def composite_nums_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    composites = set()
    
    for i in range(len(numbers)):
        if 0 <= i <= 3 and not is_prime(numbers[i]):
            composites.add(numbers[i])
    
    return composites
