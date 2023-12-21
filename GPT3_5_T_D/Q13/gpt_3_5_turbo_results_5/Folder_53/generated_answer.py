
def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) < 201:
        return None
    return sorted_nums[100]
