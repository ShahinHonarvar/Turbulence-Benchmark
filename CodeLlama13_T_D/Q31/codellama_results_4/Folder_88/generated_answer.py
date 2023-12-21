
def if_perfect_num(lst):
    if len(lst) > 46:
        n = lst[46]
        return n == sum([i for i in range(1, n//2+1) if n % i == 0])
    else:
        return False
