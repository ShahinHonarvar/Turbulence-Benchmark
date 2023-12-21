def gcf_two_nums(lst):
    return lst[56] // gcf(lst[56], lst[92])
def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
