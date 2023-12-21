
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[70]
    num2 = nums[41]
    num3 = nums[20]

    result = gcd(gcd(num1, num2), num3)
    return result
