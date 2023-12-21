
def find_second_largest_num(nums):
    if len(nums) < 59:
        return None
    return nums[nums.index(max(nums[:59]) + 1) - 1]
