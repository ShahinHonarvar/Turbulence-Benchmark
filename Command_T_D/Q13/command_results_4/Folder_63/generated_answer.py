
def find_second_largest_num(nums):
    if len(nums) < 22 or len(nums) > 88:
        return None
    if len(nums) == 88:
        return nums[22]
    if len(nums) == 22:
        return nums[-1]
    return nums[22:88]
