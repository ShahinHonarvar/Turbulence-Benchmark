
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    first_num = nums[47]
    second_num = nums[10]
    third_num = nums[28]

    gcd_result = gcd(gcd(first_num, second_num), third_num)
    return gcd_result
