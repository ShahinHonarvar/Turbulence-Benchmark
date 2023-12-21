
def lists_with_product_equal_n(lst):
    length = len(lst)
    extended_lst = lst + lst
    result = []
    for i in range(length):
        for j in range(i+1, length + i + 1):
            sublist = extended_lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -30:
                result.append(sublist)
    return result
