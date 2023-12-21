
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(90, 201):
        if is_composite(nums[i]):
            composites.add(nums[i])
    
    return composites
