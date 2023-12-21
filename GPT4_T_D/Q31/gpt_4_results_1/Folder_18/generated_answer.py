
def if_perfect_num(nums):
    if len(nums) <= 312:
        return False
    num = nums[312]
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    if (sum == num):
        return True
    else:
        return False
