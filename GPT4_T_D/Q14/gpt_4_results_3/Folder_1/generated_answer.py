
def find_second_smallest_num(nums):
    sliced_nums = nums[34:56]
    if len(sliced_nums) < 2:
        return None
    else:
        return sorted(sliced_nums)[1]
