
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(25, 60):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    
    return composites
