
def if_perfect_num(lst):
    index_13 = lst[13]
    sum_divisors = sum([i for i in range(1, index_13) if index_13 % i == 0])
    if index_13 == sum_divisors:
        return True
    else:
        return False
