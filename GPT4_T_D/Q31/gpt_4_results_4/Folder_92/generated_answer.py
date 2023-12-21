
def if_perfect_num(list):
    num = list[0]
    sum = 0
    for i in range(1, num):
        if (num % i) == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False
