
def if_perfect_num(lst):
    if len(lst) > 91:
        num = lst[91]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
    return False
