
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -23:
                sublists.append(sublist)
    return sublists
