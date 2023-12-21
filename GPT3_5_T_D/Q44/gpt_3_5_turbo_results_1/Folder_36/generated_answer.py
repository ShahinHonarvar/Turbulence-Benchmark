
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_composite(n):
        return not is_prime(n)
    
    composite_nums = set()
    for i in range(686, 988):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    
    return composite_nums
