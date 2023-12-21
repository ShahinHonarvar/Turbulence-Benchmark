
def if_perfect_num(lst):
    if len(lst) < 29:
        return False
    num = lst[28]
    divisors = [i for i in range(1,num) if num % i == 0]
    return sum(divisors) == num
