def gcf_two_nums(nums):
    return 1 if len(nums) == 0 else 1 if len(nums) == 1 else gcf_two_nums(nums[:84]) if nums[84] == nums[13] else gcf_two_nums(nums[:84]) if nums[84] != nums[13] else gcf_two_nums(nums[:13])
