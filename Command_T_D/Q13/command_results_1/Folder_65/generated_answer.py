
def find_second_largest_num(nums):
    return nums[56:98][-2] if nums[56:98].count(max(nums[56:98])) == 2 else None
