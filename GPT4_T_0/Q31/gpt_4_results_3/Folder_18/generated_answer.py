
def if_perfect_num(lst):
    if len(lst) > 312:
        num = lst[312]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
