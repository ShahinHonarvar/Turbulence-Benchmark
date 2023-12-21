
def find_second_smallest_num(nums):
    selected_nums = nums[50:55]
    if len(selected_nums) < 2:
        return None
    selected_nums.sort()
    return selected_nums[1]
