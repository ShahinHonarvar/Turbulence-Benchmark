
def lists_with_product_equal_n(l):
    def product(s):
        p = 1
        for i in s:
            p *= i
        return p

    size = len(l)
    l = l + l
    result = []
    for i in range(size):
        for j in range(i+1, i+size+1):
            if product(l[i:j]) == 990:
                result.append(l[i:j])
    return result
