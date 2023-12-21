
def find_second_largest_num(nums):
    if len(nums)<=1:
        return None
    nums_slice = nums[0:6]
    nums_slice.sort()
    return nums_slice[-2] if len(nums_slice)>1 else None
