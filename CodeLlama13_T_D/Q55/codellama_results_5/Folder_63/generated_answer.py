
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i+1]
        product = 1
        while product < n and (i + len(sublist)) < len(lst):
            sublist.append(lst[i + len(sublist)])
            product *= lst[i + len(sublist)]
        if product == n:
            result.append(sublist)
    return result
