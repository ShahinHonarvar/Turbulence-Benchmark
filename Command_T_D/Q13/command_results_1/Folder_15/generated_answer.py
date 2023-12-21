
def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    max_num = max(nums)
    index = nums.index(max_num)
    if index == 0 or index == len(nums) - 1:
        return None
    return nums[index - 1] if index == 1 or index == len(nums) - 2 else nums[index + 1]
