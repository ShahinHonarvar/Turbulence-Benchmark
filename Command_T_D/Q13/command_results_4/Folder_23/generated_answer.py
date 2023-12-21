
def find_second_largest_num(nums):
    idx = [i for i in range(len(nums)) if nums[i] > nums[0]]
    return nums[idx[-2]] if idx else None
