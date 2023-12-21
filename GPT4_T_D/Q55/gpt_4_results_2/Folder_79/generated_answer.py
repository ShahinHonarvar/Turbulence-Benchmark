
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        for start in range(n):
            sublist = [lst[(start + i) % n] for i in range(length)]
            product = 1
            for x in sublist:
                product *= x
            if product == -83:
                result.append(sublist)
    return result
