
def if_perfect_num(lst):
    num = lst[4]
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    return sum == num
