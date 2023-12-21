
def if_perfect_num(lst):
    if len(lst) > 37:
        num = lst[37]
        factors = [k for k in range(1, num) if num % k == 0]
        if sum(factors) == num:
            return True
    return False
