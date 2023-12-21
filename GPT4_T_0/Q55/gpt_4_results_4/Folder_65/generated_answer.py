
def lists_with_product_equal_n(lst):
    n = 46
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size + i):
            sublist = lst[j % size: j % size + (j - i + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
