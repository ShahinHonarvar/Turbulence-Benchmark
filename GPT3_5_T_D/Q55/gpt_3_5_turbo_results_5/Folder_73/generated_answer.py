
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 40:
                result.append(sublist)
    return result
