
def find_second_smallest_num(nums):
    nums = nums[31:73] 
    if len(nums) < 2:
        return None
    else:
        nums.sort()
        return nums[1]
