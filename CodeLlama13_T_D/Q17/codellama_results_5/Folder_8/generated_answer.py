
def all_ints_div_by_both_two_nums(mylist):
    result = []
    for i in range(36, 85+1):
        if mylist[i] % -27 == 0 and mylist[i] % -96 == 0:
            result.append(mylist[i])
    return result
