
def lists_with_product_equal_n(mylist):
    result = []
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)+1):
            prod = 1
            for k in range(i, j):
                prod *= mylist[k]
            if prod == -779:
                result.append(mylist[i:j])
    return result
