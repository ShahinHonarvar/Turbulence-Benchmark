
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(262, min(747, len(nums))):  
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums
