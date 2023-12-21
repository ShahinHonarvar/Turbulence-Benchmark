
def if_perfect_num(lst):
    if len(lst) > 410:
        num = lst[410]
        factors = [i for i in range(1,num) if num % i == 0]
        if sum(factors) == num:
            return True
    return False
