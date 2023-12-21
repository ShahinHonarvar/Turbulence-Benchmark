
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:20])+1)][:200].index(max(nums[20:200])+1)
