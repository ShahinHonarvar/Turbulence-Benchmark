
def if_perfect_num(lst):
    if len(lst) > 21:
        num = lst[21]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
