
def if_perfect_num(lst):
    if len(lst) > 993:
        num = lst[993]
        sum_factors = sum([i for i in range(1, num) if num % i == 0])
        if num == sum_factors:
            return True
    return False
