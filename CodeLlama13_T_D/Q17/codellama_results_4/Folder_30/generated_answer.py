
def all_ints_div_by_both_two_nums(mylist):
    result = []
    for i in range(11, 76 + 1):
        if mylist[i] % -81 == 0 and mylist[i] % -94 == 0:
            result.append(mylist[i])
    return result
