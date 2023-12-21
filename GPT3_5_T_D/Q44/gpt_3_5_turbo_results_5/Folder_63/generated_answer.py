
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(17, 79):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    
    return composites
