
def find_second_largest_num(nums):
    if len(nums)>=60:
        nums=nums[25:60]
        nums.sort()
        return nums[-2]
    return None
