
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sublst = lst[i:j]
            product = 1
            for num in sublst:
                product *= num
            if product == 99:
                result.append(sublst)
    return result
