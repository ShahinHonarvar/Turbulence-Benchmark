
def gcf_two_nums(nums):
    a = nums[0]
    b = nums[1]
    
    while b:
        a, b = b, a % b
    
    return a
