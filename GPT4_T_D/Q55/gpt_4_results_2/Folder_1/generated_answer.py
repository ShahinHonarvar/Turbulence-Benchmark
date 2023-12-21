
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j] + lst[0:i] + lst[j:]
            product = 1
            for num in sublist:
                product *= num
            if product == -51:
                result.append(sublist)
    return result
