
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    index_1 = 38
    index_2 = 77
    
    num_1 = nums[index_1]
    num_2 = nums[index_2]
    
    return gcd(num_1, num_2)
