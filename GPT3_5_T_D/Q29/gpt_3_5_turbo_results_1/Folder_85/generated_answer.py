
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[38]
    num2 = nums[77]
    
    return find_gcf(num1, num2)
