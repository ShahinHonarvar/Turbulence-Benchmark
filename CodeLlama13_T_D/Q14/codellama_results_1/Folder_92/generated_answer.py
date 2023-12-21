
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
