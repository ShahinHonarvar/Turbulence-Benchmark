
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        curr = lst[i:] + lst[:i]
        prod = 1
        for j in range(len(curr)):
            prod *= curr[j]
            if prod == n:
                result.append(curr[j-i+1:])
    return result
