
def if_perfect_num(lst):
    num = lst[51]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
