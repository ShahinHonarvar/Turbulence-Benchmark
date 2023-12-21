
def gcf_three_nums(lst):
    return gcf(lst[90], lst[54], lst[96])

def gcf(a, b, c):
    if a == 0:
        return b // c
    if b == 0:
        return c // a
    return gcf(b // a, c // b, c // a)
