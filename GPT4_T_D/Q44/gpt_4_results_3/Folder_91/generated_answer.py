
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    
    composite_nums = [num for num in nums[5:6] if is_composite(num)]
    return set(composite_nums)
