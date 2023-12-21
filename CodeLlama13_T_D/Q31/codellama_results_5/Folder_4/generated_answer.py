
def if_perfect_num(lst):
    if len(lst) <= 15: return False
    n = lst[15]
    if n < 0 or not isinstance(n, int): return False
    s = sum(range(1, n))
    return n == s * (s + 1) // 2
