
def find_second_smallest_num(nums):
    if len(nums) >= 64:
        sorted_nums = sorted(nums[62:64])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None
