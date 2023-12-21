def gcf_two_nums(lst):
    return 1 if lst[17] == lst[20] else lst[17] // gcf(lst[17], lst[20])
def gcf(a, b):
    while b:
        a, b = b, a % b
    return a
