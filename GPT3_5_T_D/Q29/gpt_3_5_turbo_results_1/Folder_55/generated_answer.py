
def gcf_two_nums(nums):
    a = nums[1]
    b = nums[2]
    
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        
    return a
