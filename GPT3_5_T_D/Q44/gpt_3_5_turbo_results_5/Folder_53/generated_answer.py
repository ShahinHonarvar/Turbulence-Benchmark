
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_composite(num):
        return not is_prime(num)
    
    composite_set = set()
    
    for i in range(222, 223):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
            
    return composite_set
