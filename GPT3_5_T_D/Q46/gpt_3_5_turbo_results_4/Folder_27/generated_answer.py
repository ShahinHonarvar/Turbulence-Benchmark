
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    index_76 = nums[76]
    index_64 = nums[64]
    index_28 = nums[28]

    gcf = find_gcf(index_76, index_64)
    gcf = find_gcf(gcf, index_28)

    return gcf
