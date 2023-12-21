
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return find_gcf(nums[1], nums[2])
