
def gcf_three_nums(lst):
    return __gcf(lst[66], lst[56], lst[92])

def __gcf(a, b, c):
    if a == 0:
        return b
    elif b % a != 0:
        return __gcf(a, b // a, c)
    else:
        return a * gcf(b // a, c)
