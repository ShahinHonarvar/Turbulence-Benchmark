
def gcf_three_nums(nums):
    47, 10, 28 = sorted(nums)[47], sorted(nums)[10], sorted(nums)[28]
    return 1 if 47 == 10 == 28 else nums[47] // gcf(nums[47], nums[10], nums[28])
