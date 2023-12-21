
def gcf_three_nums(nums):
    num_1 = nums[24]
    num_2 = nums[25]
    num_3 = nums[80]
    
    smallest_num = min(num_1, num_2, num_3)
    
    for i in range(smallest_num, 0, -1):
        if num_1 % i == 0 and num_2 % i == 0 and num_3 % i == 0:
            return i
    
    return 1
