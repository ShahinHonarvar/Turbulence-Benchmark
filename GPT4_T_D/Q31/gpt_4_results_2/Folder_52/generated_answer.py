
def if_perfect_num(lst):
    num = lst[478] if len(lst) > 478 else None
    if num is not None:
        divisors = []
        for i in range(1,num):
            if (num % i)==0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
    return False
