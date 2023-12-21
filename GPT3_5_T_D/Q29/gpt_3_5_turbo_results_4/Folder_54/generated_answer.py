
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[56]
    num2 = nums[92]

    return gcd(num1, num2)
