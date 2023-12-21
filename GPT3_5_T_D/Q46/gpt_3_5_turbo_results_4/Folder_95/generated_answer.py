
def gcf_three_nums(nums):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    a = nums[87]
    b = nums[20]
    c = nums[36]

    gcf = gcd(a, gcd(b, c))
    return gcf
