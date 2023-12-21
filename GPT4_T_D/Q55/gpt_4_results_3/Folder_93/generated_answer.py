
def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []

    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j] if j != n-1 else lst[i:] + [lst[0]]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                res.append(sublist)
        if i != 0:
            for j in range(0, i):
                sublist = [lst[i]] + lst[0:j+1]
                product = 1
                for num in sublist:
                    product *= num
                if product == -91:
                    res.append(sublist)
    return res
