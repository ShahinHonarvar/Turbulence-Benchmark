
def if_perfect_num(lst):
    return lst[72] == sum(d for d in range(1, int(lst[72])**0.5 + 1) if lst[72] % d == 0)
