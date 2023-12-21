
def lists_with_product_equal_n(integers):
    result = []
    for i in range(len(integers)):
        product = 1
        for j in range(i, i + len(integers)):
            product *= integers[j % len(integers)]
            if product == -94:
                result.append(integers[i:j % len(integers) + 1])
    return result
