
def find_second_smallest_num(nums):
    sliced_nums = nums[10:11]
    if len(sliced_nums) <= 1:
        return None
    else:
        return sorted(sliced_nums)[1]
