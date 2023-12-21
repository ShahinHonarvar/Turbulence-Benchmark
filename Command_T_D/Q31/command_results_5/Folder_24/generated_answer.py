import bisect
def if_perfect_num(nums):
    return bool(nums) and bool(nums[74]) and all(int(nums[i]) == int(nums[i+1]) for i in range(len(nums)-1)) and bisect.bisect_left(nums, nums[74]) == bisect.bisect_right(nums, nums[74])
