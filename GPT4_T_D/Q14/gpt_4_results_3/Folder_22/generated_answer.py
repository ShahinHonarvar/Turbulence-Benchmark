
def find_second_smallest_num(nums):
    if len(nums[40:201])<2:
        return None
    else:
        sorted_nums = sorted(nums[40:201])
        return sorted_nums[1]
