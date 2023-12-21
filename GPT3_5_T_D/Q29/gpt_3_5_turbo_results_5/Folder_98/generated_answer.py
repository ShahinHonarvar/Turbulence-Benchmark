
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[0]
    num2 = nums[9]
    gcf = find_gcf(num1, num2)
    return gcf
