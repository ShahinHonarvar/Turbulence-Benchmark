
def find_second_largest_num(distinct_nums):
    sorted_nums = sorted(distinct_nums)
    return sorted_nums[75:89][-1] if len(sorted_nums[75:89]) > 0 else None
