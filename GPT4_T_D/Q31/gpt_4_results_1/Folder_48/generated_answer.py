
def if_perfect_num(lst):
    if len(lst) <= 247:
        return False
    num = lst[247]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
