
def find_second_largest_num(nums):
    if len(nums[28:39]) >= 2:
        sorted_nums = sorted(nums[28:39])
        return sorted_nums[-2]
    else:
        return None
