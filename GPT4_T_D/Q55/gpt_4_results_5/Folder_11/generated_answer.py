
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    if n <= 1:
        return []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = lst[i:j] if j<=n else lst[i:] + lst[:j-n]
            if len(sublist) == 0:
                continue
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -15:
                result.append(sublist)
    return result
