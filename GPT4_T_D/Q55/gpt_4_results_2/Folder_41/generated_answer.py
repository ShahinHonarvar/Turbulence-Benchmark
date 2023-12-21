
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst
    result = []
    for L in range(1, n + 1):
        for i in range(n):
            sublist = lst[i: i + L]
            product = 1
            for number in sublist:
                product *= number
            if product == -20:
                result.append(sublist[:L])
    return result
