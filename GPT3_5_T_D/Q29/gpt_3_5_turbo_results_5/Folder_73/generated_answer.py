
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return find_gcf(nums[51], nums[27])
