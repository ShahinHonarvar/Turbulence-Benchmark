
def sum_ints_div_by_either_nums(mylist):
    result = 0
    for i in range(len(mylist)):
        if mylist[i] % -2 == 0 or mylist[i] % 3 == 0:
            result += mylist[i]
    return result
