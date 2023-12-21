
def lists_with_product_equal_n(lst):
    sublist = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, i+len(lst)):
            product *= lst[j%len(lst)]
            if product == -83:
                sublist.append([lst[k%len(lst)] for k in range(i, j+1)])
            elif product < -83 and abs(product) > abs(-83):
                break
    return sublist
