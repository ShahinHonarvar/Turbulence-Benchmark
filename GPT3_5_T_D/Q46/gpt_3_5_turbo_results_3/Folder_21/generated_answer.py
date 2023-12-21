
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    idx1 = 412
    idx2 = 932
    idx3 = 337

    num1 = nums[idx1]
    num2 = nums[idx2]
    num3 = nums[idx3]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf
