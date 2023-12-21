
def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    result = []
    n = len(lst)

    for i in range(n):
        for j in range(i+1, n+1):
            if product(lst[i:j]) == 51:
                result.append(lst[i:j])

    return result
