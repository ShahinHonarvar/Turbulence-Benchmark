
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i+1]
        product = 1
        while product <= 851:
            if len(sublist) == 0:
                break
            product *= sublist.pop()
            if product == 851:
                result.append(sublist)
    return result
