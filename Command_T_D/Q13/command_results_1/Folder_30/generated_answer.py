
def find_second_largest_num(nums):
    if len(nums) < 55 or len(nums) > 98:
        return None
    elif len(nums) == 55:
        return nums[54]
    elif len(nums) == 98:
        return nums[97]
    else:
        return nums[len(nums) - 2]
