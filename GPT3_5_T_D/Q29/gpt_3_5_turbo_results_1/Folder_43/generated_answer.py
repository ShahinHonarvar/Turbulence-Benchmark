
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return gcd(nums[59], nums[93])
