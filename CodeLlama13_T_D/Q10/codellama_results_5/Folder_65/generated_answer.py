
def all_odd_ints_exclusive(mylist):
    result = []
    for i in range(42, 87):
        if mylist[i] % 2 != 0:
            result.append(mylist[i])
    return result
