
def if_perfect_num(list):
    num = list[2]
    sum = 0
    for i in range(1,num):
        if num % i ==0:
            sum += i
    if num == sum:
        return True
    else:
        return False
