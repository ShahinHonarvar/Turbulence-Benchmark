
def find_second_smallest_num(nums):
    if len(nums) >= 310 and len(nums) <= 370:
        sorted_nums = sorted(nums[310:371])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None
