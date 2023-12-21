def gcf_two_nums(lst):
    return 1 if lst[129] == 1 or lst[582] == 1 else gcf(lst[129], lst[582])
def gcf(a, b):
    if a == 1 or b == 1:
        return 1
    return gcf(b // a, a)
