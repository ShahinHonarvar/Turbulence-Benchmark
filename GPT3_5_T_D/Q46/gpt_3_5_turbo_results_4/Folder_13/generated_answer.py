
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    return find_gcf(find_gcf(nums[991], nums[244]), nums[974])
