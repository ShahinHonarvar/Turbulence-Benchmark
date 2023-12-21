
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num_95 = nums[95]
    num_85 = nums[85]
    
    return gcd(num_95, num_85)
