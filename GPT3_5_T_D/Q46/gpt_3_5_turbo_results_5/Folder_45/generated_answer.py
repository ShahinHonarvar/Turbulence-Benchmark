
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    nums_46 = nums[46]
    nums_84 = nums[84]
    nums_23 = nums[23]

    gcf_46_84 = gcd(nums_46, nums_84)
    gcf_46_84_23 = gcd(gcf_46_84, nums_23)

    return gcf_46_84_23
