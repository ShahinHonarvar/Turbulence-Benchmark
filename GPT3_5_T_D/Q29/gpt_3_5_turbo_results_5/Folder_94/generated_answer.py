
def gcf_two_nums(nums):
    def calculate_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    return calculate_gcf(nums[91], nums[45])
