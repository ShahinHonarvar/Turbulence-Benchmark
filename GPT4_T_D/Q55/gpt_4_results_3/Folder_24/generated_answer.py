
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    if size == 0:
        return result
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j+1]
            product = 1
            for number in sublist:
                product *= number
            if product == -89:
                result.append(sublist)
            if product == -89 and j==size-1 and i!=0:
                sublist_2 = lst[0:i]
                product_2 = 1
                for number in sublist_2:
                    product_2 *= number
                if product_2 == 1:
                    result.append(sublist + sublist_2)
    return result
