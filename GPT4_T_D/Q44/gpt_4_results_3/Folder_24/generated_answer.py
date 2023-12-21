
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    result = {num for i,num in enumerate(nums[34:56]) if is_composite(num)}
    return result
