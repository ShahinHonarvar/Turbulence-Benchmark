
def find_second_largest_num(nums):
    nums.sort()
    return nums[nums.count(max(nums[:100])-1)+1:nums.count(max(nums[100:200]))+1]
