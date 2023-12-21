
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size + i):
            sublist = lst[i: j + 1]
            if sublist:
                product = 1
                for num in sublist:
                    product *= num
                if product == -46:
                    sublists.append(sublist)
    return sublists
