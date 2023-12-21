
def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    
    while b != 0:
        (a, b) = (b, a % b)
    
    while c != 0:
        (a, c) = (c, a % c)

    return a
