
def if_perfect_num(lst):
    if len(lst) <= 90:
        return False
    n = lst[90]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and n // i > i:
            return True
    return False
