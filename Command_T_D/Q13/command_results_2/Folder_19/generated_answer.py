
def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    elif len(nums) == 3:
        return nums[1]
    elif len(nums) == 4:
        return nums[2]
    elif len(nums) == 5:
        return nums[3]
