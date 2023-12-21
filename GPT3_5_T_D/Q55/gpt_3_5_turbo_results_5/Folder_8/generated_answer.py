
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == -41:
                result.append(lst[i:index+1])
    return result
