
def gcf_three_nums(nums):
    index_1 = 85
    index_2 = 36
    index_3 = 54
    
    num_1 = nums[index_1]
    num_2 = nums[index_2]
    num_3 = nums[index_3]
    
    while True:
        if num_1 % num_2 == 0 and num_1 % num_3 == 0:
            return num_1
