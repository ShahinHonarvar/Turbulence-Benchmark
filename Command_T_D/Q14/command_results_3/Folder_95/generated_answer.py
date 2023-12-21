def find_second_smallest_num(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    low, high = sorted(nums)[75], sorted(nums)[85]
    if high == low:
        return nums[high]
    else:
        return nums[low:high+1][-2]
