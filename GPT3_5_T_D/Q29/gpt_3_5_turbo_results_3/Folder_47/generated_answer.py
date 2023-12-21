
def gcf_two_nums(nums):
    num_1 = nums[28]
    num_2 = nums[17]
    
    while num_2 != 0:
        temp = num_2
        num_2 = num_1 % num_2
        num_1 = temp
    
    return num_1
