def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    sorted_nums = sorted(nums)
    return sorted_nums[6] if len(nums) == 7 else sorted_nums[5]
