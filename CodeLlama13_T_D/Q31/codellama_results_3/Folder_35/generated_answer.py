
def if_perfect_num(lst):
    if len(lst) <= 993:
        return False
    else:
        n = lst[993]
        return all(i for i in range(2, int(n ** 0.5) + 1) if n % i == 0) and sum(i for i in range(1, int(n ** 0.5) + 1) if n % i == 0) == n
