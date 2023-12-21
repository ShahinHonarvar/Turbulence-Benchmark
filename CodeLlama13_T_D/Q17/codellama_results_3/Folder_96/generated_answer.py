
def all_ints_div_by_both_two_nums(mylist):
    result = []
    for i in range(50, 201):
        if mylist[i] % -34 == 0 and mylist[i] % 64 == 0:
            result.append(mylist[i])
    return result
