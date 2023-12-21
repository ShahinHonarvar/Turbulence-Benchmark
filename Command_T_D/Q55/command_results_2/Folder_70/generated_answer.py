def lists_with_product_equal_n(lst):
    result = []
    lst = lst[:]
    for x in range(1, len(lst)):
        if lst[x] == 32:
            result.append(lst[x:])
            lst = lst[:x] + lst[x+1:]
    return result
