
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n <= 1:  
            return False
        for i in range(2, ((n//2) + 1)):
            if n % i == 0: 
                return True
        return False

    return set(n for n in nums[111:112] if is_composite(n))
