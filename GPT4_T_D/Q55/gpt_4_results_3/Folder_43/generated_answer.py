
def lists_with_product_equal_n(lst):
    result = []
    ll = len(lst)
    lst = lst + lst
    for i in range(ll):
        for j in range(i + 1, i + ll + 1):
            product = 1
            for ele in lst[i:j]:
                product *= ele
            if product == -26:
                result.append(lst[i:j])
    return result
