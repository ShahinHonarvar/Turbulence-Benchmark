
def find_second_smallest_num(nums):
    if len(nums[22:89]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[22:89])
        return sorted_nums[1]
