
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sub = lst[j%n:(j%n)+1] + lst[:max(j-n+1,0)]
            prod = 1
            for x in sub:
                prod *= x
            if prod == -69:
                result.append(sub)
    return result
