
def if_perfect_num(nums):
    num = nums[194]
    divisorSum = 0
    for i in range(1, num):
        if num % i == 0:
            divisorSum += i
    if divisorSum == num:
        return True
    else:
        return False
