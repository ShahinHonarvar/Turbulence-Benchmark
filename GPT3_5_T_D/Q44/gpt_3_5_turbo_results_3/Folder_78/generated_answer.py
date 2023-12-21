
def composite_nums_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    start_index = 70
    end_index = 84
    composites = set()
    
    for i in range(start_index, end_index + 1):
        if not is_prime(numbers[i]):
            composites.add(numbers[i])
            
    return composites
