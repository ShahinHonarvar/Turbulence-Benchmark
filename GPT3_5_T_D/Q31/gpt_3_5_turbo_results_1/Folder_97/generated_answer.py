
def if_perfect_num(lst):
    num = lst[132]
    if num < 0:
        return False
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    if sum(factors) == num:
        return True
    return False
