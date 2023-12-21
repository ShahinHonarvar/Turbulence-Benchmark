
def lists_with_product_equal_n(lst):
    sublists = []
    length = len(lst)
    for i in range(length):
        product = 1
        j = i
        sublist = []
        while product < 45:
            product *= lst[j%length]
            sublist.append(lst[j%length])
            j += 1
        if product == 45:
            sublists.append(sublist)
    return sublists
