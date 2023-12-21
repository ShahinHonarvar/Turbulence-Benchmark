
def find_second_smallest_num(nums):
    if len(nums) < 14:
        return None
    else:
        selected_nums = nums[13:69]
        if len(selected_nums) < 2:
            return None
        else:
            sorted_nums = sorted(selected_nums)
            return sorted_nums[1]
