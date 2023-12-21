
def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    result = max(nums[:10])
    if len(nums) > 10:
        result = nums[len(nums) - 1]
    return result
