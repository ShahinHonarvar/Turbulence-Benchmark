def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[37])-1] if nums[nums.index(sorted(nums)[37])-1] != nums[nums.index(sorted(nums)[38])-1] else None
