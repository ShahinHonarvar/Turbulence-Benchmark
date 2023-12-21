
def if_perfect_num(lst):
    num = lst[56]
    sum1 = 0
    for i in range(1, num):
        if(num % i == 0):
            sum1 += i
    return True if sum1 == num else False
