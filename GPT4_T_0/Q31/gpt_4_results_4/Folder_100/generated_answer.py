
def if_perfect_num(lst):
    num = lst[99]
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        return True
    else:
        return False
