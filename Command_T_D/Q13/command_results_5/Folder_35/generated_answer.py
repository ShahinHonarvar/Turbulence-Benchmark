
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:30])+1)+30:nums.index(max(nums[30:48])+1)+48]
