
def find_second_largest_num(nums):
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] == max(nums[:i] + nums[i+1:]):
            return nums[i]
    return None
