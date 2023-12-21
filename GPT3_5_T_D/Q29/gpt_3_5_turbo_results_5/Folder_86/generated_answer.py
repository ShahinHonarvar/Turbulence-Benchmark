
def gcf_two_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = nums[793]
    num2 = nums[449]
    return gcd(num1, num2)
