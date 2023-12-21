
def all_left_truncatable_prime(nums):
    x = nums[42]
    result = []
    
    for i in range(1, x+1):
        if is_left_truncatable_prime(i):
            result.append(i)
            
    return sorted(result)
