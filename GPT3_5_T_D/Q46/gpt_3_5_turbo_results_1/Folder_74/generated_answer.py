
def gcf_three_nums(nums):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x

    num1 = nums[99]
    num2 = nums[95]
    num3 = nums[80]

    gcd1 = find_gcf(num1, num2)
    gcd2 = find_gcf(gcd1, num3)

    return gcd2
