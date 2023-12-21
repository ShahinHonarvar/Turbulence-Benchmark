
def find_second_largest_num(nums):
    if len(nums) <= 30:
        return None
    if len(nums) <= 200:
        return nums[-2]
    return nums[200]
