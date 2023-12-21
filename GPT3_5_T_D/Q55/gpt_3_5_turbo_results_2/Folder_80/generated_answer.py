
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product = 1

    for i in range(n):
        if lst[i] != 0:
            product = 1
            for j in range(i, i+n):
                k = j % n
                product *= lst[k]

                if product == 43:
                    result.append(lst[i:k+1])
                    break

    return result
