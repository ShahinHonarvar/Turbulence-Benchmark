
def if_perfect_num(lst):
    if len(lst) <= 43:
        return False
    num = lst[43]
    sum_fact = 0
    for i in range(1, num):
        if num % i == 0:
            sum_fact += i
    if sum_fact == num:
        return True
    else:
        return False
