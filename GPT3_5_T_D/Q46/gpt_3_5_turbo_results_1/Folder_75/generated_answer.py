
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    index1 = 70
    index2 = 98
    index3 = 22

    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]

    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)

    return gcf2
