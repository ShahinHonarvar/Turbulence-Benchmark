
def if_perfect_num(lst):
    if len(lst) > 194:
        num = lst[194]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
