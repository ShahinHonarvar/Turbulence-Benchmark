import bisect
def if_perfect_num(nums):
    return all(n == 2*nums[bisect.bisect_left(nums,n)] for n in nums)
