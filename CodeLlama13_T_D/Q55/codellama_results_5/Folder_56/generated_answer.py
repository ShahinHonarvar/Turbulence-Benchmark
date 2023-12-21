
def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        curr_prod = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            curr_prod *= lst[j]
            if curr_prod == n:
                result.append(sublist)
            elif curr_prod > n:
                break
            else:
                sublist.append(lst[j])
    return result
