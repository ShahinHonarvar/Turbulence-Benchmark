
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = nums[17]
    num2 = nums[20]
    return gcd(num1, num2)
