
def if_perfect_num(list_of_nums):
    num = list_of_nums[96]
    sum = 0
    for i in range (1, num):
        if(num % i == 0):
            sum = sum + i
    if (sum == num):
        return True
    else:
        return False
