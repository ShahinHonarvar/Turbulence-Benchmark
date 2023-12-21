
def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for i in range(n):
        product = lst[i]
        if product == 40:
            results.append([product])
        for j in range(i+1, (i + n) % n):
            product *= lst[j % n]
            if product == 40:
                results.append(lst[i:j+1])
    return results
