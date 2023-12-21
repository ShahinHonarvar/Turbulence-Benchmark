
def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for i in range(n):
        for j in range(i+1, n+1):
            sub = lst[i:j]
            product = 1
            for num in sub:
                product *= num
            if product == -36:
                results.append(sub)
            if len(sub)==n-1: break

    # check for lists which includes both tail and head
    for i in range(n-1, 0, -1):
        sublist = lst[i:] + lst[:n-i]
        product = 1
        for num in sublist:
            product *= num
            if product == -36:
                results.append(sublist)
    return results
