
def gcf_two_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    return gcd(nums[860], nums[307])
