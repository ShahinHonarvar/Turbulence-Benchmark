def lists_with_product_equal_n(l):
    res = []
    for i in range(len(l)):
        if l[i] == 6:
            j = i
            while j < len(l):
                if l[j] == 6:
                    break
                j += 1
            res += [[l[i]] + l[i + 1:j]]
    return res
