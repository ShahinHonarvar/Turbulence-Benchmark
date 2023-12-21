
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        if len(nums) == 2:
            return nums[0]
        else:
            return nums[1]
