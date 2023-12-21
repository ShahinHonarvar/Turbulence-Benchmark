
def gcf_two_nums(nums):
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    return compute_gcd(nums[56], nums[92])
