
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = lst[j % n: j % n + (j - i + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == 51:
                result.append(sublist)
    return result
