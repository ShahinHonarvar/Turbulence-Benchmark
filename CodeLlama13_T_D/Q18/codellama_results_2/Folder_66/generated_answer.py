
def sum_ints_div_by_either_nums(mylist):
    result = 0
    for i in range(58, 82):
        if mylist[i] % 10 == 0 or mylist[i] % 55 == 0:
            result += mylist[i]
    return result
