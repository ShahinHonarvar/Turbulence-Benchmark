
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    product = 1

    for i in range(size):
        product = lst[i]
        if product == -56:
            result.append([product])

        for j in range(i + 1, size):
            product *= lst[j]
            if product == -56:
                result.append(lst[i:j+1])

            if product == 0:
                break

    return result
