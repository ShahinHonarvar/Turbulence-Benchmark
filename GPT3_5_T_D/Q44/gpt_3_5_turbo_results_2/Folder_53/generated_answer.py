
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composites = set()
    for num in numbers[222:223]:
        if is_composite(num):
            composites.add(num)
    
    return composites
