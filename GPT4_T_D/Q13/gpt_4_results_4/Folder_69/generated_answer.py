
def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    else:
        sorted_nums = sorted(nums[32:36], reverse=True)
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
