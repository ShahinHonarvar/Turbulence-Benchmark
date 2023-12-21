
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[87]
    num2 = nums[20]
    num3 = nums[36]

    gcf = gcd(gcd(num1, num2), num3)

    return gcf
