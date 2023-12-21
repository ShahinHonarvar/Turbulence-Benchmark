
def lists_with_product_equal_n(lst):
    len_lst = len(lst)
    result = []
    for i in range(len_lst):
        for j in range(1, len_lst+1):
            sublist = lst[i:i+j]
            if i+j > len_lst:
                sublist += lst[:i+j-len_lst]
            product = 1
            for num in sublist:
                product *= num
            if product == -26:
                result.append(sublist)
    return result
