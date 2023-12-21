
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composites = set()
    
    for index, number in enumerate(numbers[15:40], start=15):
        if is_composite(number):
            composites.add(number)
            
    return composites
