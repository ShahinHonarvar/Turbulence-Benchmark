
def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(n):
            num = lst[(i+j)%n]
            product *= num
            if product == -97:
                sublist = lst[i:i+j+1]
                sublists.append(sublist)
    return sublists
