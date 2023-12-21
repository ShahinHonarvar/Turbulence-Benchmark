
def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    if len(nums) == 6:
        return nums[-2]
    return nums[5:7][-2]
