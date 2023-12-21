
def gcf_three_nums(nums):
    num1 = nums[59]
    num2 = nums[93]
    num3 = nums[84]
    
    smaller = min(num1, num2, num3)
    
    gcf = 1
    
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i
            
    return gcf
