
def find_second_largest_num(nums):
    nums = sorted(nums)
    for i in range(15, 40):
        if i == len(nums) - 2:
            return nums[i]
    return None
