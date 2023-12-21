
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i+1, length+1):
            sub_lst = lst[i:j]
            product = 1
            for num in sub_lst:
                product *= num
            if product == 76:
                result.append(sub_lst)
    return result
