
def lists_with_product_equal_n(lst):
    res = []
    length = len(lst)
    lst.extend(lst[:length-1])
    for i in range(length):
        for j in range(i+1, i+length):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -22:
                res.append(sublist)
    return res
