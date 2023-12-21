
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composite_nums = set()
    for i, num in enumerate(numbers[59:98], start=59):
        if is_composite(num):
            composite_nums.add(num)
    
    return composite_nums
