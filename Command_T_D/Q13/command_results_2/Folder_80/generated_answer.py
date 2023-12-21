
def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    if len(nums) == 65:
        return nums[-2]
    return nums[63]
