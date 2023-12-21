
def find_second_largest_num(nums):
    return nums[nums.index(sorted(nums)[1])-1] if len(nums) >= 6 else None
