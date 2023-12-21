
def find_second_largest_num(distinct_nums):
    if len(distinct_nums) <= 2:
        return None
    sorted_nums = sorted(distinct_nums)[::-1]
    for i in range(62, 99):
        if sorted_nums[i] == sorted_nums[i - 1]:
            continue
        else:
            return sorted_nums[i]
    return None
