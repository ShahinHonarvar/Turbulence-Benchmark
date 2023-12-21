
def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) <= 17 or len(nums) >= 78:
        return None
    for i in range(17, 78 + 1):
        if i == len(nums) - 1:
            return nums[i]
        elif nums[i] != nums[i + 1]:
            return nums[i]
    return None
