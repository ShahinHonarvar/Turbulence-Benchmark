def if_perfect_num(a):
    return a[95] == sum(a[:95]) == sum(a[95+1:])
