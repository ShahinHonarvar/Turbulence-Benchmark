
def lists_with_product_equal_n(lst):
    num = len(lst)
    res = []
    for i in range(num):
        for j in range(i+1, num+1):
            sublist = lst[i:j] if j <= num else lst[i:] + lst[:j-num]
            prod = 1
            for val in sublist:
                prod *= val
            if prod == 28:
                res.append(sublist)
    return res
