
def find_second_smallest_num(nums):
    if len(nums) <= 98:
        return None
    sorted_nums = sorted(nums[55:99])
    for i in range(len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
