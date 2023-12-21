
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst)+1):
            sub = lst[i:i+j]
            if i+j > len(lst):
                sub += lst[:(i+j)%len(lst)]
            product = 1
            for num in sub:
                product *= num
            if product == -65:
                result.append(sub)
    return result
