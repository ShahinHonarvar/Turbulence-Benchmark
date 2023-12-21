
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    return find_gcf(find_gcf(nums[15], nums[51]), nums[76])
