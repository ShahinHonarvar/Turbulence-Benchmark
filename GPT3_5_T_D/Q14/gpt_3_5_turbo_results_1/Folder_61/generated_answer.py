
def find_second_smallest_num(lst):
    unique_nums = list(set(lst))
    sorted_nums = sorted(unique_nums)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
