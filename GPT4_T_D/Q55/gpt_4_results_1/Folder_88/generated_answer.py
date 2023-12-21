
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for l in range(1, len(lst) + 1):
            sublist = lst[i:i+l]
            if i + l > len(lst):
                sublist = sublist + lst[:(i+l) % len(lst)]
            product = 1
            for num in sublist:
                product *= num
            if product == -56:
                result.append(sublist)
    return result
