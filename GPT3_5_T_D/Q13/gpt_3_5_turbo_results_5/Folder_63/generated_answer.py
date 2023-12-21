
def find_second_largest_num(nums):
    sorted_nums = sorted(nums[22:89], reverse=True)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
