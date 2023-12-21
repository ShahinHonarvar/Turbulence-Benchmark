
def find_second_smallest_num(nums):
    sorted_nums = sorted(nums[25:88])
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None
