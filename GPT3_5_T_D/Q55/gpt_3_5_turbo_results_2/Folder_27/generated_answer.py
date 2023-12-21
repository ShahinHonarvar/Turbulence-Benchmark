
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i, length):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -82:
                result.append(sublist)
    return result
