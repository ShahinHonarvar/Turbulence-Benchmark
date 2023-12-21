
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num54 = nums[54]
    num13 = nums[13]
    
    return gcd(num54, num13)
