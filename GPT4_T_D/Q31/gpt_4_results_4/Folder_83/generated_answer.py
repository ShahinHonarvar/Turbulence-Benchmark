
def if_perfect_num(lst):
    index_95 = lst[95]
    sum_of_divisors = sum([i for i in range(1, index_95) if index_95 % i == 0])
    if sum_of_divisors == index_95:
        return True
    else:
        return False
