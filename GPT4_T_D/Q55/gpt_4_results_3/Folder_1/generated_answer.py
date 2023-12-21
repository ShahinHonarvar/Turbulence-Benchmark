
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = lst[i:j] + lst[0:(i+j)%n] if (i+j) > n else lst[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == -51:
                if sublist not in result:
                    result.append(sublist)
    return result
