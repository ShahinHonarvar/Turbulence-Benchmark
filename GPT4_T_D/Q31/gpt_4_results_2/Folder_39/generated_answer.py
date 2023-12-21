
def if_perfect_num(lst):
    num = lst[59]
    sum_div = sum([i for i in range(1, num) if num % i == 0])
    if sum_div == num:
        return True
    else:
        return False
