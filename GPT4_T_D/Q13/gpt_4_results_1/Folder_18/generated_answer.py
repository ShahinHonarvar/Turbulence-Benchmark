
def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    sorted_nums = sorted(nums[35:50], reverse=True)
    if len(sorted_nums) == 1:
        return None
    else:
        return sorted_nums[1]
