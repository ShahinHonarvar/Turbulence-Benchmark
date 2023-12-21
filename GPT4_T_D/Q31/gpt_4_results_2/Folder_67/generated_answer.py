
def if_perfect_num(numList):
    if len(numList) < 44:
        return False
    num = numList[43]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
