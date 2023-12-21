
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j+1]
            if sublist and (sublist[-1] == -1 or sublist[0] == -1):
                if sublist[0] == -1:
                    sublist = sublist[1:] + sublist[:1]
                result.append(sublist)
    return result
