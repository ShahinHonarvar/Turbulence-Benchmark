
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i+1]
        product = 1
        while product < 36 and len(sublist) <= len(lst):
            product *= sublist[-1]
            sublist.append(sublist[-1])
        if product == 36:
            result.append(sublist)
    return result
