
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = lst[i:j]
            if sublist and (eval('*'.join(map(str, sublist)))) == -8:
                sublists.append(sublist)
    return sublists
