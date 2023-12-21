
def find_second_smallest_num(nums):
    sub_nums = nums[75:89]
    sorted_nums = sorted(set(sub_nums))
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
