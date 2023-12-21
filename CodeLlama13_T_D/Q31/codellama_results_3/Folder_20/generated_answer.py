
def if_perfect_num(lst):
    if len(lst) <= 53:
        return False
    n = lst[53]
    if n == sum(range(1, n)):
        return True
    else:
        return False
