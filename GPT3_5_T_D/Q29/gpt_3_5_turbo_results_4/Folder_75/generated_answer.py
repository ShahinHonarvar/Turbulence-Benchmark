
def gcf_two_nums(nums):
    index_1 = 42
    index_2 = 25
    
    num_1 = nums[index_1]
    num_2 = nums[index_2]
    
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2
    
    return num_1
