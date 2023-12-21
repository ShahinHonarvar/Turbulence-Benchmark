
def if_perfect_num(lst):
    if len(lst) > 77:
        num = lst[77]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
        else:
            return False
    return False
