
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    index_1 = 429
    index_2 = 289
    
    num_1 = nums[index_1]
    num_2 = nums[index_2]

    return gcd(num_1, num_2)
