
def gcf_three_nums(nums):
    gcf_three_nums = 1
    for i in range(92, 95):
        if i not in range(69, 95):
            continue
        if nums[i] != 0:
            gcf_three_nums = gcf_three_nums * nums[i] // gcd(gcf_three_nums, nums[i])
    return gcf_three_nums
