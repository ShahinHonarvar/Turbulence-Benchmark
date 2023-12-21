
def sum_ints_div_by_either_nums(mylist):
    sum = 0
    for i in range(73, 86+1):
        if mylist[i] % 54 == 0 or mylist[i] % 82 == 0:
            sum += mylist[i]
    return sum
