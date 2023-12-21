
def find_second_largest_num(nums):
    sorted_nums = sorted(nums[:5], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
