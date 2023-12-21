
def if_perfect_num(lst):
    if len(lst) > 321:
        num = lst[321]
        sum1 = 0
        for i in range(1, num):
            if(num % i == 0):
                sum1 = sum1 + i
        if sum1 == num:
            return True
        else:
            return False
    return False
