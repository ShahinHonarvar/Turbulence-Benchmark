
def gcf_three_nums(nums):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(gcf(nums[6], nums[7]), nums[8])
