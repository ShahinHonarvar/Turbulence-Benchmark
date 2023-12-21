
def lists_with_product_equal_n(lst):
    size = len(lst)
    lst *= 2
    result = []
    for i in range(size):
        for j in range(i+1, i+size+1):
            if j-i <= size:
                sublist = lst[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == -61:
                    result.append(sublist)
    return result
