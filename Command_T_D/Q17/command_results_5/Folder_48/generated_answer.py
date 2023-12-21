
import bisect

def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[bisect.bisect_left(nums, 306):bisect.bisect_left(nums, 957)] if x%982==x%319==0]
