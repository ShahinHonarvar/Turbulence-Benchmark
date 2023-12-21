
def if_perfect_num(lst):
    num = lst[15]
    div_sum = sum([i for i in range(1, num) if num % i == 0])
    if div_sum == num:
        return True
    else:
        return False
