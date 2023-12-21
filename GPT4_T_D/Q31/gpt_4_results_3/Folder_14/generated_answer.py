
def if_perfect_num(lst):
    if len(lst) > 17:
        num = lst[17]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
