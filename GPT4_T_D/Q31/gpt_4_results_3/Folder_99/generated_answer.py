
def if_perfect_num(lst):
    if len(lst) > 733:
        num = lst[733]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
