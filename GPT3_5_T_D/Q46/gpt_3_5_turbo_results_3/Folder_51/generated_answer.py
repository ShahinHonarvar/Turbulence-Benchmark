
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num_1 = nums[21]
    num_2 = nums[69]
    num_3 = nums[41]
    
    gcf = gcd(num_1, gcd(num_2, num_3))
    return gcf
