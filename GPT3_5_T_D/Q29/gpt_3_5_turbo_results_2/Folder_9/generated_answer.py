
def gcf_two_nums(nums):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return find_gcf(nums[84], nums[63])
