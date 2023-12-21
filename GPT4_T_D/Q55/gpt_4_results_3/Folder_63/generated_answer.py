
def lists_with_product_equal_n(lst):
    n = len(lst)
    extended_lst = lst + lst
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = extended_lst[i:j]
            product = 1
            for l in sublist:
                product *= l
            if product == 96:
                result.append(sublist)
    return result
