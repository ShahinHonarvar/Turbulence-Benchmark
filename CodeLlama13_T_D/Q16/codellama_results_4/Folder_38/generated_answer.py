
def sum_even_ints_inclusive(mylist):
    result = 0
    for i in range(22,64):
        if mylist[i] % 2 == 0:
            result += mylist[i]
    return result
