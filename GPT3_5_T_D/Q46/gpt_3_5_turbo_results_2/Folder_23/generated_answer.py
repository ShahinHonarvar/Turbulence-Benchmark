
def gcf_three_nums(nums):
    num_1 = nums[31]
    num_2 = nums[25]
    num_3 = nums[80]
    
    smaller = min(num_1, num_2, num_3)
    gcf = 1
    
    for i in range(1, smaller+1):
        if num_1 % i == 0 and num_2 % i == 0 and num_3 % i == 0:
            gcf = i
    
    return gcf
