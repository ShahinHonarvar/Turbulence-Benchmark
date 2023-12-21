
def find_second_smallest_num(nums):
    if len(nums)<988:
        return None
    else:
        sorted_nums = sorted(nums[686:988])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
