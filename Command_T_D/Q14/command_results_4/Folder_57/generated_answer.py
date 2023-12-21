def find_second_smallest_num(nums):
    result = sorted(nums)[19]
    if len(nums) < 30 or nums[result] == nums[20]:
        return None
    result = nums[result]
    return result
