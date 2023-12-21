
def if_perfect_num(lst):
    if len(lst) > 64:
        num = lst[64]
        factors = [x for x in range(1,num) if num%x == 0]
        return sum(factors) == num
    else:
        return False
