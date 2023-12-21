
def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    
    lst = 2*lst
    ret = []
    for i in range(len(lst)//2):
        for j in range(i+1, len(lst)):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
                if product > 851:
                    break
            if product == 851:
                ret.append(sublist)
    return ret
