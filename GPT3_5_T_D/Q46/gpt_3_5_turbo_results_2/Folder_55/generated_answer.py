
def gcf_three_nums(nums):
    num1 = nums[9]
    num2 = nums[6]
    num3 = nums[2]

    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    gcf = gcd(num1, gcd(num2, num3))
    return gcf
