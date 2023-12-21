
def if_perfect_num(lst):
    num = lst[84]
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    if sum_factors == num:
        return True
    else:
        return False
