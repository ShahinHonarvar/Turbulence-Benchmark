
def gcf_three_nums(nums):
    num_1 = nums[31]
    num_2 = nums[25]
    num_3 = nums[80]
    
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2
    
    while num_3:
        num_1, num_3 = num_3, num_1 % num_3
    
    return num_1
