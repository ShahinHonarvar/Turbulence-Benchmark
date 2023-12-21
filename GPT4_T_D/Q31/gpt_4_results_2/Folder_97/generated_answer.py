
def if_perfect_num(lst):
    num = lst[132] if len(lst) > 132 else None
    if num:
        sum_factors = sum([i for i in range(1, num) if num % i == 0])
        if sum_factors == num:
            return True
    return False
