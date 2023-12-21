
def find_second_largest_num(nums):
    if len(nums) < 40:
        return None
    elif len(nums) < 80:
        return nums[-2]
    else:
        return nums[len(nums) - 80]
