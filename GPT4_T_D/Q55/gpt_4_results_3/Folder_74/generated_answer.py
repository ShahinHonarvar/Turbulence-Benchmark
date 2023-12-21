
def lists_with_product_equal_n(lst):
    sublist = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + i):
            temp = lst[j%len(lst)] 
            if j == i:
                product = temp
            else:
                product *= temp
            if product == 51:
                sublist.append(lst[i:j%len(lst)+1])
    return sublist
