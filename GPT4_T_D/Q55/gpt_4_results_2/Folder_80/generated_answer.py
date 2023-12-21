
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sub_lst = lst[i:j]
            product = 1
            for x in sub_lst:
                product *= x
            if product == 43:
                result.append(sub_lst)
    return result
