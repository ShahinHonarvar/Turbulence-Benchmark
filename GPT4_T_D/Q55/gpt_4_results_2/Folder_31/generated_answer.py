
def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    lst = lst + lst  # Double the list to make it circular
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            temp = lst[i:j]
            product = 1
            for num in temp:
                product *= num
            if product == -16:
                result.append(temp)
    return result
