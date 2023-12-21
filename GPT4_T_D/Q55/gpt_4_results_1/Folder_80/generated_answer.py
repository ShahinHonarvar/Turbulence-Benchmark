
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    if n == 0:
        return result

    for l in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + l] if i + l <= n else lst[i:] + lst[:(i + l)%n]
            product = 1
            for num in sublist:
                product *= num
            if product == 43:
                result.append(sublist)

    return result
