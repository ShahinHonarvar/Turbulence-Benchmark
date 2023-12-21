
def lists_with_product_equal_n(lst):
    results = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1] + lst[0:max(0,i+j+1-n)]
            product = 1
            for num in sublist:
                product *= num
            if product == -938:
                results.append(sublist)
    return results
