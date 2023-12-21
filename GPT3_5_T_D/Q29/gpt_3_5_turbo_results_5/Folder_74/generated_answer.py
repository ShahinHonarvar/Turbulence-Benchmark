
def gcf_two_nums(nums):
    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcf(nums[36], nums[85])
