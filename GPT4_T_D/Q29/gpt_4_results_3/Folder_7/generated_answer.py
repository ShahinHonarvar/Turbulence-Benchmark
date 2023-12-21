
def gcf_two_nums(nums):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(nums[224], nums[663])
