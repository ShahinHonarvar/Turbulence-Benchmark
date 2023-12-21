
def find_second_largest_num(nums):
    if 66 <= len(nums) - 1:
        relevant_nums = nums[66:94]
        if len(relevant_nums) > 1:
            relevant_nums.sort()
            return relevant_nums[-2]
    return None
