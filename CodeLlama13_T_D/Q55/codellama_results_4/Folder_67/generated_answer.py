
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)+1):
            sublist = lst[i:j]
            if len(sublist) > 1 and prod(sublist) == n:
                result.append(sublist)
    return result
