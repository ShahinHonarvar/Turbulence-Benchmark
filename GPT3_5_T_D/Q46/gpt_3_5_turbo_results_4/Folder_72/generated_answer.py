
def gcf_three_nums(nums):
    x = nums[44]
    y = nums[91]
    z = nums[42]
    
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x

    while x != z:
        if x > z:
            x -= z
        else:
            z -= x
    
    return x
