
def find_second_smallest_num(distinct_nums):
    if len(distinct_nums) < 8:
        return None
    sorted_nums = sorted(distinct_nums)
    second_smallest = sorted_nums[7]
    for i in range(4, 8):
        if sorted_nums[i] == second_smallest:
            continue
        else:
            return None
    return second_smallest
