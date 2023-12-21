
def gcf_two_nums(nums):
    a = nums[59]
    b = nums[93]
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a
