
def find_second_smallest_num(nums):
    nums = sorted(nums)
    for i in range(40, 81):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            continue
        return nums[i]
    return None
