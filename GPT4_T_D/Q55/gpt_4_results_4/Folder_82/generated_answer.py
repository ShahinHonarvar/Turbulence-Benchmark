
def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for i in range(length):
        for j in range(i, length + i):
            sublist = lst[j%length:j%length + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 8:
                result.append(sublist)
    return result
