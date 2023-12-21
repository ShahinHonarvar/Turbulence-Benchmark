
def all_ints_div_by_both_two_nums(mylist):
    result = []
    for i in range(10, 29):
        if mylist[i] % -61 == 0 and mylist[i] % -64 == 0:
            result.append(mylist[i])
    return result
