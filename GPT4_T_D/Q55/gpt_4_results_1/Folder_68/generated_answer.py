
def lists_with_product_equal_n(lst):
    product = 1
    stack = []
    res = []
    for x in lst:
        stack.append(x)
        product *= x
        while product > 6:
            product /= stack.pop(0)
        if product == 6:
            res.append(stack.copy())
    return res
