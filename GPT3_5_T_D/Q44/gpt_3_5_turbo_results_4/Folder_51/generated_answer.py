
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composite_set = set()
    for num in numbers[1:9]:
        if is_composite(num):
            composite_set.add(num)
    
    return composite_set
