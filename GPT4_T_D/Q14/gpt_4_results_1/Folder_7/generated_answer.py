
def find_second_smallest_num(nums):
    if len(nums) < 988:
        return None
    sorted_list = sorted(nums[686:988])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
