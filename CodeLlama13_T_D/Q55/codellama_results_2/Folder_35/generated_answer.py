
def lists_with_product_equal_n(list):
    sublists = []
    for i in range(len(list)):
        for j in range(i+1, len(list)+1):
            product = 1
            for k in range(i, j):
                product *= list[k]
            if product == n:
                sublists.append(list[i:j])
    return sublists
