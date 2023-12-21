
def find_second_smallest_num(nums):
    if len(nums[56:67]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[56:67])
        return sorted_nums[1]
