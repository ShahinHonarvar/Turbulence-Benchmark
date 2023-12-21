
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 2:
        return None
    if len(nums) == 2:
        return nums[1]
    if nums[0] == nums[-1]:
        return nums[1]
    return nums[nums.index(max(nums[:-1])) + 1]
