
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    for i in range(n):
        for j in range(1, n+1):
            sublist = lst[i:j] if i < j else lst[i:] + lst[:j]
            product = 1
            for k in sublist:
                product *= k
            if product == 40:
                result.append(sublist)

    return result
