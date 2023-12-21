def if_perfect_num(a):
    return a[790] == sum(a[:790]) == sum(a[790+1:])
