
def find_second_smallest_num(nums):
    if len(nums) < 99:
        return None
    else:
        selected_nums = nums[91:100]
        selected_nums.sort()
        if len(selected_nums) < 2:
            return None
        else:
            return selected_nums[1]
