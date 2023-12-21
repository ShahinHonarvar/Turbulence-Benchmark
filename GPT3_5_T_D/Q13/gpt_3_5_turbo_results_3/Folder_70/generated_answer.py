
def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    sorted_nums = sorted(nums[28:33], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
