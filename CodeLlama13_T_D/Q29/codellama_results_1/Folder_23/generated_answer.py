
def gcf_two_nums(lst):
    return __gcf(lst[48], lst[74])

def __gcf(a, b):
    if a == 0:
        return b
    return __gcf(b % a, a)
