
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        sublist = [lst[i]]
        product = lst[i]
        if product == -18:
            sublists.append(sublist)
        for j in range(i+1, i+size):
            k = j % size
            sublist.append(lst[k])
            product *= lst[k]
            if product == -18:
                sublists.append(list(sublist))
    return sublists
