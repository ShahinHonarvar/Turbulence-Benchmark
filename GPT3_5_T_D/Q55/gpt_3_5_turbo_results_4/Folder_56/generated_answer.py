
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == -65:
            result.append(lst[:i+1])
    for i in range(1, n):
        product //= lst[i-1]
        if product == -65:
            result.append(lst[i:])
    return result
