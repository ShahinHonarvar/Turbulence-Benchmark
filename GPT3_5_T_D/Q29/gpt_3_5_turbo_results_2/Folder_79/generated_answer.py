
def gcf_two_nums(nums):
    a = nums[85]
    b = nums[51]
    
    while b != 0:
        a, b = b, a % b
    
    return a
