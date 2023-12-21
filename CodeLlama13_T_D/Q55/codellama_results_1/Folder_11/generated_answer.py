
def lists_with_product_equal_n(lst):
    n = -15
    result = []
    for i in range(len(lst)):
        product = 1
        temp = lst[i:] + lst[:i]
        for j in range(i, len(temp)):
            product *= temp[j]
            if product == n:
                result.append(temp[i:j+1])
    return result
