def gcf_two_nums(nums):
    return 1 if nums[69] == 1 or nums[41] == 1 else gcf_two_nums(nums)[0] // gcf_two_nums(nums)[1] // gcf_two_nums(nums)[0] // gcf_two_nums(nums)[1]
