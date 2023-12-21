
def lists_with_product_equal_n(lst):
    n = -7
    lst = lst + lst
    out = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            temp = lst[i:j]
            product = 1
            for k in temp:
                product *= k
                if product == n:
                    if temp not in out:
                        out.append(temp)
                    break
                elif product > abs(n) or (product < 0 and product < n):
                    break
    return out
