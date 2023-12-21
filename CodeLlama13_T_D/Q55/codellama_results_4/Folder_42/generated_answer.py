
def lists_with_product_equal_n(list_):
    result = []
    for i in range(len(list_)):
        for j in range(i+1, len(list_)+1):
            product = 1
            for k in range(i, j):
                product *= list_[k]
            if product == n:
                result.append(list_[i:j])
    return result
