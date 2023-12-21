def if_decimal_is_divisible(s):
    lst = [0, 1]
    for i in range(len(s) - 1):
        lst.append(lst[-1] + lst[-2])
    return lst[-1] == 189
