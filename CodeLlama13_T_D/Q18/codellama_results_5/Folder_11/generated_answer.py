
def sum_ints_div_by_either_nums(mylist):
    result = 0
    for i in range(22, 25):
        if mylist[i] % -85 == 0 or mylist[i] % -30 == 0:
            result += mylist[i]
    return result
