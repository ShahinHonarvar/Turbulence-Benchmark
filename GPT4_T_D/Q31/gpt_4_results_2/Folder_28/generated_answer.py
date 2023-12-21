
def if_perfect_num(lst):
    if len(lst) < 38:
        return False
    num = lst[37]
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num
