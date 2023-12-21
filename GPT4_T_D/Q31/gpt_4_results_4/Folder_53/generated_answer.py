
def if_perfect_num(lst):
    if len(lst) < 74:
        return False
    num = lst[73]
    divisors = [x for x in range(1, num) if num % x == 0]
    if sum(divisors) == num:
        return True
    else:
        return False
