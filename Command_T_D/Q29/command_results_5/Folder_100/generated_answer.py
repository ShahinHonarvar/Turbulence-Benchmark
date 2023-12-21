def gcf_two_nums(nums):
    return 1 if len(nums) == 0 else 1 if len(nums) == 1 else gcf_two_nums(nums[:96]) if nums[96] != 0 else gcf_two_nums(nums[:32]) if nums[32] != 0 else gcf_two_nums(nums[:96]) if nums[32] != 0 else gcf_two_nums(nums[:32])
