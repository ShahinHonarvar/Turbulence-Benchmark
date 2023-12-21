
def if_perfect_num(lst):
    index_43 = lst[43]
    sum_divisors = 0
    for i in range(1, index_43):
        if index_43 % i == 0:
            sum_divisors += i
    if sum_divisors == index_43:
        return True
    else:
        return False
