
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    indices = [341, 238, 374]
    gcd_result = nums[indices[0]]

    for index in indices[1:]:
        gcd_result = gcd(gcd_result, nums[index])

    return gcd_result
