
def composite_nums_between_indices(nums):
    composites = set()
    
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    for i in range(15, min(40, len(nums))):
        if is_composite(nums[i]):
            composites.add(nums[i])
            
    return composites
