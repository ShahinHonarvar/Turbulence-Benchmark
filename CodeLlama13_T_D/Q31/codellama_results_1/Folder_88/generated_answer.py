
def if_perfect_num(lst):
    n = lst[46]
    s = sum(range(1, int(n**0.5) + 1))
    return n == s * (s + 1) / 2
