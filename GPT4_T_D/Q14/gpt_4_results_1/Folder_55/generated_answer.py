
def find_second_smallest_num(nums):
    if len(nums[10:11]) < 2:
        return None
    else:
        return sorted(nums[10:11])[1]
