
def all_ints_div_by_num(myList):
    result = []
    for i in range(len(myList)):
        if myList[i] % 9 == 0:
            result.append(myList[i])
    return result
