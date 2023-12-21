
def find_second_smallest_num(nums):
    try:
        sorted_nums = sorted(nums[56:58])
    except IndexError:
        return None
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
