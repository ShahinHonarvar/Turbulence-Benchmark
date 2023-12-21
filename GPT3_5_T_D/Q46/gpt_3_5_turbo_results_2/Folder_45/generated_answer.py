
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[46]
    num2 = nums[84]
    num3 = nums[23]

    if num1 == 0 or num2 == 0 or num3 == 0:
        return 0

    result = gcd(num1, num2)
    result = gcd(result, num3)

    return result
