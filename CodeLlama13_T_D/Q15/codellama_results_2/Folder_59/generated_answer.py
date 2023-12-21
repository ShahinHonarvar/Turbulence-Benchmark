
def sum_odd_ints_inclusive(mylist):
    return sum(mylist[i] for i in range(0, 10) if mylist[i] % 2 != 0)
