
def if_perfect_num(lst):
    number = lst[100]
    sum1 = 0
    for i in range(1, number):
        if(number % i == 0):
            sum1 = sum1 + i
    if (sum1 == number):
        return True
    else:
        return False
