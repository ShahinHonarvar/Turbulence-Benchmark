
def lists_with_product_equal_n(myList):
    result = []
    for i in range(len(myList)):
        product = 1
        tempList = []
        for j in range(i, len(myList)):
            product *= myList[j]
            if product == n:
                result.append(tempList + [myList[j]])
            elif product > n:
                break
            else:
                tempList.append(myList[j])
    return result
