
def if_perfect_num(lst):
    n = lst[54]
    factors = [i for i in range(1, n) if n % i == 0]
    if sum(factors) == n:
        return True
    else:
        return False
