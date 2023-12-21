
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    a = nums[87]
    b = nums[95]
    return gcd(a, b)
