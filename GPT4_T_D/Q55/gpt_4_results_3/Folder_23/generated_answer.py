
def lists_with_product_equal_n(lst):
    from math import prod
    size = len(lst)
    result = []
    for start in range(size):
        for end in range(start+1, size+2):
            sublist = lst[start:end]
            if end > size:
                sublist += lst[0:end-size]
            if prod(sublist) == -95:
                result.append(sublist)
    return result
