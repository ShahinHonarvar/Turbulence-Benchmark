
def gcf_two_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    num1 = nums[78]
    num2 = nums[93]
    gcd = find_gcd(num1, num2)
    return gcd
