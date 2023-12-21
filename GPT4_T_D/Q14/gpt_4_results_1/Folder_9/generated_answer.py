
def find_second_smallest_num(nums):
    if len(nums) < 200:
        return None
    else:
        nums_slice = sorted(nums[70:201])
        if len(nums_slice) < 2:
            return None
        else:
            return nums_slice[1]
