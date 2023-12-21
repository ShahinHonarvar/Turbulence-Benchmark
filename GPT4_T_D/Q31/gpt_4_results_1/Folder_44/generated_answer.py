
def if_perfect_num(lst):
    if len(lst) > 828:
        num = lst[828]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
        else:
            return False
    else:
        return False
