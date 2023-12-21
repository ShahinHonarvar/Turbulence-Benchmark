
def if_perfect_num(lst):
    if len(lst) <= 746:
        return False
    else:
        num = lst[746]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
