
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            if len(sublist) > 0 and np.prod(sublist) == 83:
                result.append(sublist)
    return result
