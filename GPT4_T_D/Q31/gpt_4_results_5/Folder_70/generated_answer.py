
def if_perfect_num(lst):
    if lst[845]:
        num = lst[845]
        sum_factors = sum([i for i in range(1, num) if num % i == 0])
        if sum_factors == num:
            return True
    return False
