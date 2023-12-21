
def sum_even_ints_inclusive(mylist):
    total = 0
    for i in range(111, 112):
        if mylist[i] % 2 == 0:
            total += mylist[i]
    return total
