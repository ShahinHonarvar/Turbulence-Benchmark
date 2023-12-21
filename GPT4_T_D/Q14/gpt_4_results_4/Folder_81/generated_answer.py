
def find_second_smallest_num(nums):
    start_index = 10
    end_index = 101
    selected_nums = nums[start_index:end_index]
    if len(selected_nums) < 2:
        return None
    else:
        sorted_nums = sorted(selected_nums)
        return sorted_nums[1]
