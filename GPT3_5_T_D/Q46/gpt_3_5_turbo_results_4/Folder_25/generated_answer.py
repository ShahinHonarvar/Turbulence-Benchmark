
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = nums[32]
    num2 = nums[54]
    num3 = nums[13]
  
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
