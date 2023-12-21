
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 19, 94 and 78
    # use the Euclidean algorithm to find the greatest common divisor
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    nums = [my_list[19], my_list[94], my_list[78]]
    gcf = 1
    for i in range(len(nums)):
        if gcf == 1:
            gcf = nums[i]
        else:
            gcf = gcd(gcf, nums[i])
    return gcf
