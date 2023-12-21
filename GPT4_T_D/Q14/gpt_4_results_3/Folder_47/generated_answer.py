
def find_second_smallest_num(nums):
    if len(nums[22:64]) < 2:
        return None
    else:
        nums_slice = sorted(nums[22:64])
        return nums_slice[1]
