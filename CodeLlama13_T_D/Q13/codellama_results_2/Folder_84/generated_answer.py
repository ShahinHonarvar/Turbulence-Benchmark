
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    
    nums = sorted(nums)
    second_largest = nums[-2]
    for i in range(43, 87):
        if nums[i] == second_largest:
            return nums[i]
    return None
