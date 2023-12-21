
def lists_with_product_equal_n(lst):
    sublists = []
    lst_extended = lst + lst
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst_extended[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 2:
                sublists.append(sublist)
    return sublists
