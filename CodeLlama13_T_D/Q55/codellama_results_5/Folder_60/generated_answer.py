
def lists_with_product_equal_n(myList):
    result = []
    for i in range(len(myList)):
        product = 1
        sublist = [myList[i]]
        j = (i + 1) % len(myList)
        while j != i:
            product *= myList[j]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
            else:
                sublist.append(myList[j])
            j = (j + 1) % len(myList)
    return result
