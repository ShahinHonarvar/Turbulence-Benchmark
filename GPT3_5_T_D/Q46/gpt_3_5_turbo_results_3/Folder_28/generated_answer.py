
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    index_1 = nums[99]
    index_2 = nums[63]
    index_3 = nums[74]
    gcf = gcd(gcd(index_1, index_2), index_3)
  
    return gcf
