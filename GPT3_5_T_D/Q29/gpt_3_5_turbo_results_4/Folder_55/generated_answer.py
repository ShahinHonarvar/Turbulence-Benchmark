
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = nums[1]
    b = nums[2]
    
    return find_gcf(a, b)
