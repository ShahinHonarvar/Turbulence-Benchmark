
def sum_ints_div_by_either_nums(mylist):
    result = 0
    for i in range(10):
        if mylist[i] % 6 == 0 or mylist[i] % -3 == 0:
            result += mylist[i]
    return result
