
def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(1, n+1):
            if i < j:
                temp = lst[i:j]
            else:
                temp = lst[i:] + lst[:j]
            product = 1
            for number in temp:
                product *= number
            if product == -33:
                res.append(temp)
    return res
