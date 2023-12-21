
def gcf_three_nums(nums):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    index1 = 341
    index2 = 238
    index3 = 374

    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf
