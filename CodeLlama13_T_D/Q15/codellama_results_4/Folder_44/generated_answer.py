
def sum_odd_ints_inclusive(mylist):
    odds = []
    for i in range(13, 69):
        if mylist[i] % 2 == 1:
            odds.append(mylist[i])
    return sum(odds)
