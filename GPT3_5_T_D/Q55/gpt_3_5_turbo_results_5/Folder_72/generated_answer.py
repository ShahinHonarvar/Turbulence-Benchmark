
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        j = i
        while product != 10:
            product *= lst[j]
            if product == 10:
                result.append(lst[i:j+1])
            j = (j+1) % n
    return result
