
def find_second_largest_num(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[1]
    return nums[10:100][-2]
