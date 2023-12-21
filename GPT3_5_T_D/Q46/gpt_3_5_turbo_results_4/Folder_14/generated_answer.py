
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    index1 = 17
    index2 = 88
    index3 = 35
    
    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf
