
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(59, 98):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    
    return composites
