def if_decimal_is_divisible(s):
    lst = [(0, 1)]
    for c in s:
        if lst[-1][0] % 2 == 1:
            lst += [(lst[-1][1] + 1, lst[-1][0] + 1)]
        else:
            lst += [(lst[-1][1], lst[-1][0] + 1)]
    return lst[-1][0] % 2 == 1
