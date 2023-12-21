
def find_second_largest_num(nums):
    if not nums or len(nums) < 51:
        return None
    relevant_nums = nums[29:52]
    relevant_nums.sort()
    return relevant_nums[-2] if len(relevant_nums) > 1 else None
