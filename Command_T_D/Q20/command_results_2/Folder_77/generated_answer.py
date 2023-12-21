import bisect
def find_n_th_smallest_num(nums):
    return bisect.bisect_left(nums, nums[len(nums)-10:])[9]
