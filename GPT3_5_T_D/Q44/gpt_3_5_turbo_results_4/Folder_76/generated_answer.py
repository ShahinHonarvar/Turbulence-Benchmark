
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composites = set()
    for i, num in enumerate(nums[639:976], 639):
        if is_composite(num):
            composites.add(num)
    
    return composites
