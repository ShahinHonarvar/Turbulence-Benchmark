
def find_second_largest_num(distinct_nums):
    if len(distinct_nums) >= 34:
        sorted_list = sorted(distinct_nums[31:35])
        return sorted_list[-2]
    return None
