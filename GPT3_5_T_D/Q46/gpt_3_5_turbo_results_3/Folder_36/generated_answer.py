
def gcf_three_nums(nums):
    num_1 = nums[427]
    num_2 = nums[761]
    num_3 = nums[148]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcf = gcd(gcd(num_1, num_2), num_3)
    return gcf
