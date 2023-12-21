
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    a = nums[49]
    b = nums[53]
    
    return find_gcf(a, b)
