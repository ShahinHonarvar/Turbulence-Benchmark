
def return_binary_or_hexa(tup):
    lst = list(range(tup[0] + 1, tup[6] - 1))
    lst = list(set(lst) - set(tup[0:6]))
    lst = str(sum(lst))
    if len(lst) % 2:
        return lst
    else:
        return lst.zfill(len(lst) // 2)
