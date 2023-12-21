
def composite_nums_between_indices(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    composites = set()
    for i in range(35, 50):
        if is_prime(numbers[i]) == False:
            composites.add(numbers[i])
    
    return composites
