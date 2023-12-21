import fractions
def gcf_two_nums(nums):
    idx = 56
    while idx < 88:
        if fractions.gcd(nums[idx], nums[88]) > 1:
            break
        idx += 1
    return fractions.gcd(nums[idx], nums[88])
