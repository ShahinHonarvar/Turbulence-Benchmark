
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:n]
    result = []
    for i in range(n):
        product = 1
        j = i
        while j < i+n and product != -8:
            product *= lst[j]
            j += 1
        if product == -8:
            result.append(lst[i:j])
    return result
