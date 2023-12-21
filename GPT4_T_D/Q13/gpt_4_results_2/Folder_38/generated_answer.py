
def find_second_largest_num(nums):
    if len(nums) < 23:
        return None
    else:
        current_nums = nums[22:64]
        current_nums.sort(reverse=True)
        return current_nums[1] if len(current_nums) > 1 else None
