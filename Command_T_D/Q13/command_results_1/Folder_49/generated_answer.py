
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:80]))+1:nums.index(max(nums[80:200]))+1]
