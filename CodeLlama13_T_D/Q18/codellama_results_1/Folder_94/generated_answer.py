
def sum_ints_div_by_either_nums(mylist):
    result = 0
    for i in range(93, 95):
        if mylist[i] % -53 == 0 or mylist[i] % -91 == 0:
            result += mylist[i]
    return result
