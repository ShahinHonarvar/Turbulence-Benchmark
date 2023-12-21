
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:i+1]
        if len(sublist) > 1 and prod(sublist) == n:
            result.append(sublist)
    return result
