
def lists_with_product_equal_n(list):
    sublists = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            product = 1
            for k in range(i, j+1):
                product *= list[k]
            if product == -95:
                sublists.append(list[i:j+1])
    return sublists
