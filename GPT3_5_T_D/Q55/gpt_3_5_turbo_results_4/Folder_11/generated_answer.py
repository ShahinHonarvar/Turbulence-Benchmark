
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for start in range(n):
        product = 1
        for end in range(start, start+n):
            product *= lst[end % n]
            if product == -15:
                result.append(lst[start:end+1])
    return result
