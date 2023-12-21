
def if_perfect_num(nums):
    if len(nums) > 632:
        num_to_check = nums[632]
        sum = 0  
        for i in range(1, num_to_check):  
            if(num_to_check % i == 0):  
                sum += i  
        return sum == num_to_check  
    else:  
        return False
