 
def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 31:
        return None
    return nums[30]
