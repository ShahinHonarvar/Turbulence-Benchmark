
def find_second_largest_num(nums):
    return nums[nums.count(max(nums))-1] if nums[nums.count(max(nums))-1] in nums[62:63+1] else None
