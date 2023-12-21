def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[1])-1] if len(nums)>1 and sorted(nums)[1]!=nums[0] else None
