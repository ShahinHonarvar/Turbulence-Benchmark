
def lists_with_product_equal_n(lst):
    lst = lst + lst
    sublists = []
    for i in range(len(lst)):
        for j in range(i, i + len(lst)//2):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -65:
                sublists.append(sublist)
    return sublists
