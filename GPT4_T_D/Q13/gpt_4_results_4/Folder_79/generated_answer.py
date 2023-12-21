
def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    else:
        sorted_nums = sorted(nums[4:5])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[-2]
