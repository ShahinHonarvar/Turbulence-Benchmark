
def sum_odd_ints_inclusive(mylist):
    odds = []
    for i in range(62, 100):
        if mylist[i] % 2 != 0:
            odds.append(mylist[i])
    return sum(odds)
