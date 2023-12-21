
def lists_with_product_equal_n(mylist):
    result = []
    for i in range(len(mylist)):
        sublist = mylist[i:i+len(result)+1]
        if len(sublist) <= len(mylist) and np.prod(sublist) == -54:
            result.append(sublist)
    return result
