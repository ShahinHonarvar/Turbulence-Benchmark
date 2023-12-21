def if_perfect_num(a):
    return a[80] == sum(a[:80]) == sum(a[81:])
