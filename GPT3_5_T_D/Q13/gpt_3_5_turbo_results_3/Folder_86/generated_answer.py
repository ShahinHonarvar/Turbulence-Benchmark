
def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    
    nums = sorted(nums[31:35])
    return nums[-2]
