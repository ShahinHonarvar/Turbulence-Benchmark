
def gcf_three_nums(lst):
    lst[49] = lst[46] = lst[13] = 1
    for i in range(1, min(lst) + 1):
        if lst[49] % i == lst[46] % i == lst[13] % i:
            lst[49] /= i
            lst[46] /= i
            lst[13] /= i
            break
    return lst[49]
