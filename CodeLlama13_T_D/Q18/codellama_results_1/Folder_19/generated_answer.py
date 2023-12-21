
def sum_ints_div_by_either_nums(mylist):
    total = 0
    for i in range(1, 5):
        if mylist[i] % 4 == 0 or mylist[i] % -6 == 0:
            total += mylist[i]
    return total
