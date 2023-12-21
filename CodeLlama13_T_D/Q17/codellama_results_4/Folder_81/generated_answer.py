
def all_ints_div_by_both_two_nums(mylist):
    result = []
    for i in range(10, 101):
        if mylist[i] % 10 == 0 and mylist[i] % 100 == 0:
            result.append(mylist[i])
    return result
