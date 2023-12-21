
def if_perfect_num(nums):
    if len(nums) < 30:
        return False
    
    value = nums[29]
    sum = 0
    for i in range(1, value):
        if value % i == 0:
            sum += i
    return sum == value
