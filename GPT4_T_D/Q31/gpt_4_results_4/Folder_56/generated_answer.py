
def if_perfect_num(lst):
    if len(lst) > 60:
        num = lst[60]
        factors = [i for i in range(1,num) if num%i==0]
        return sum(factors) == num
    else:
        return False
