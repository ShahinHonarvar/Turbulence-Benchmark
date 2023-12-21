
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composite_numbers = set()
    for i in range(2, 3 + 1):
        if is_composite(numbers[i]):
            composite_numbers.add(numbers[i])
    
    return composite_numbers
