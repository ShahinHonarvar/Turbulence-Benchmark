def gcf_two_nums(nums):
    gcf = 1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] != 0 and nums[j] != 0:
                gcf = gcf(gcf, nums[i] * nums[j] // gcd(nums[i], nums[j]))
    return gcf
