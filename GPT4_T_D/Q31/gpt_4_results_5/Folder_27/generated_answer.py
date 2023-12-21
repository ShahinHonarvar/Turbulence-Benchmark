
def if_perfect_num(lst):
    num = lst[56] if len(lst) > 56 else None
    if num:
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
