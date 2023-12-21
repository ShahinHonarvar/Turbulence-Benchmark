
def gcf_two_nums(nums):
    def GCF(a, b):
        while(b):
            a, b = b, a % b
        return a

    return GCF(nums[20], nums[83])
