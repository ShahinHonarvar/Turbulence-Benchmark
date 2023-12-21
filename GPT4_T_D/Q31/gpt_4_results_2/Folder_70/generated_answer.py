
def if_perfect_num(lst):
    index_num = lst[845]
    sum_factors = sum([i for i in range(1, index_num) if index_num % i == 0])
    if index_num == sum_factors:
        return True
    else:
        return False
