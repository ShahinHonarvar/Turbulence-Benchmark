def gcf_two_nums(nums):
    return 1 if nums[20] == 0 or nums[83] == 0 else nums[20] * nums[83] // gcd(nums[20], nums[83])
