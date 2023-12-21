
def if_perfect_num(lst):
    return lst[47] == sum(x for x in range(1, int(lst[47]) ** 0.5 + 1) if lst[47] % x == 0)
