
def find_second_largest_num(nums):
    if len(nums[64:67]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[64:67], reverse=True)
        return sorted_nums[1]
