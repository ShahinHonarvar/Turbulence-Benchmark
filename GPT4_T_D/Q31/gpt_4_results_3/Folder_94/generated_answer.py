
def if_perfect_num(list_num):
    num = list_num[93]
    factors = []
    for i in range(1,num):
        if num%i==0:
            factors.append(i)
    if sum(factors)==num:
        return True
    else:
        return False
