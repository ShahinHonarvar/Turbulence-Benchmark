
def if_perfect_num(lst):
    if len(lst) > 33:
        num = lst[33]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
