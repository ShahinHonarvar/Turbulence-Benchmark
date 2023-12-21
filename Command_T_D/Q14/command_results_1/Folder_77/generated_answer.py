import bisect
def find_second_smallest_num(nums):
    i = bisect.bisect_left(nums, max(nums) + 1)
    if i == len(nums) - 1:
        return None
    j = bisect.bisect_right(nums, min(nums) - 1)
    return nums[i + j - 1]
