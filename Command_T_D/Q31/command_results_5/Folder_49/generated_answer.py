def if_perfect_num(a):
    return a[68] == sum(i**2 for i in range(1, int(a[68] ** .5) + 1))
