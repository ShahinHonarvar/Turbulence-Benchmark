def lists_with_product_equal_n(a):
    if a:
        res = []
        for i in range(len(a)):
            p = 1
            while p == a[i]:
                p *= a[i]
                i += 1
            res.append(a[i:i + i])
        return res
    else:
        return []
